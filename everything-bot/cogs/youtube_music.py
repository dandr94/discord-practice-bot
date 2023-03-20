import datetime
import pprint
from collections import deque

import discord
import asyncio
from discord.ui import Button
from discord.ext import commands
from yt_dlp import YoutubeDL

YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True', 'quiet': True}
FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
FFMPEG_PATH = {'linux': 'ffmpeg'}


class Queue:
    def __init__(self):
        self.voice_channel = None
        self.queue = deque()
        self.playing_now = None
        self.playing_now_embed = None

    def add_track(self, title: str):
        self.queue.appendleft(title)

    def play_next(self):
        if not self.is_empty():
            next_track = self.queue.pop()
            self.playing_now = next_track

            return next_track

        return 0

    def return_playing_now(self):
        return self.playing_now

    def set_playing_now(self, track):
        self.playing_now = track

    def clear_queue(self):
        self.queue.clear()
        self.playing_now = None

    def is_empty(self):
        return len(self.queue) == 0

    def length(self):
        return len(self.queue)

    def get_by_id(self, id):
        return self.queue[id]


class YoutubeMusic(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        self.queue = Queue()

    async def connect(self, ctx):
        try:
            if not ctx.message.author.voice:
                await ctx.send('Error connect')

            vc = ctx.message.author.voice.channel
            self.queue.voice_channel = await vc.connect()
        except:
            pass

    def extract(self, arg):
        video = None

        with YoutubeDL(YDL_OPTIONS) as ytdl:
            try:
                video = ytdl.extract_info("ytsearch:%s" % arg, download=False)['entries'][0]
            except:
                video = ytdl.extract_info(arg, download=False)

        return video

    def return_url(self, ext):
        with YoutubeDL(YDL_OPTIONS) as ytdl:
            url = ext['url']
            return url

    async def play(self, ctx, url, video):
        self.queue.voice_channel.play(
            discord.FFmpegPCMAudio(source=url, **FFMPEG_OPTIONS),
            )

        duration = video.get('duration')

        embed = discord.Embed(title='Now Playing:',
                              description=f'{video.get("title")}',
                              colour=0xff2a2a) \
            .add_field(name='⌛ Duration:', value=datetime.timedelta(seconds=duration), inline=False) \
            .add_field(name='🙃 Requested by:', value=ctx.author.mention, inline=False) \
            .add_field(name='URL:', value=video.get('webpage_url'), inline=False) \
            .set_thumbnail(url=video.get('thumbnail'))
        # enter_btn = Button(style=discord.ButtonStyle.red, label='Enter', emoji='🚪'),
        # stop_btn = Button(style=discord.ButtonStyle.red, label='Stop', emoji='🛑'),
        # p_c_btn = Button(style=discord.ButtonStyle.success, label='Pause / Continue', emoji='⏯️'),
        # skip_btn = Button(style=discord.ButtonStyle.success, label='Skip', emoji='⏭️')
        # embed.add_field(name='Enter', value=enter_btn, inline=True)
        # embed.add_field(name='Stop', value=stop_btn, inline=True)
        # embed.add_field(name='Pause / Continue', value=p_c_btn, inline=True)
        # embed.add_field(name='Skip', value=skip_btn, inline=True)

        first_message = await ctx.send(
            embed=embed
            )

        self.queue.playing_now_embed = first_message

        title = video.get('title')
        self.queue.set_playing_now(title)

        while self.queue.voice_channel.is_playing:
            response = await self.bot.wait_for('button_click', check=lambda message: message.author == ctx.author)

            if response.component.label == 'Enter':
                await self.queue.playing_now_embed.edit(embed=embed, compnents=[])
                self.leave(ctx)
                await response.respond(content='Bot has entered the voice channel.')
            elif response.component.label == 'Stop':
                await self.queue.playing_now_embed.edit(embed=embed, components=[
                    Button(style=discord.ButtonStyle.red, label='Enter', emoji='🚪')])
                self.stop(ctx)
                await response.respond(content='🛑 Stopped')
                return
            elif response.component.label == 'Pause / Continue':
                if self.queue.voice_channel.is_playing():
                    self.queue.voice_channel.pause()
                    await response.respond(content='⏯️ Paused')
                elif self.queue.voice_channel.is_pause():
                    self.queue.voice_channel.resume()
                    await response.respond(content='⏯️ Resumed')
                return
            elif response.component.label == 'Skip':
                await self.queue.playing_now_embed.edit(embed=embed, components=[])
                await response.respond(content='⏭️ Skipped')
                self.skip(ctx)

    def skip(self, ctx):
        asyncio.run_coroutine_threadsafe(self.queue.playing_now_embed.edit(components=[]), self.bot.loop)
        if self.queue.voice_channel.is_playing():
            self.queue.voice_channel.pause()
        if not self.queue.is_empty():
            next_track = self.queue.play_next()
            url = self.return_url(next_track)
            asyncio.run_coroutine_threadsafe(self.play(ctx, url, next_track), self.bot.loop)
            if self.queue.playing_now_embed is not None:
                self.queue.playing_now_embed = None
        else:
            asyncio.run_coroutine_threadsafe(ctx.send("Queue is empty!", delete_after=3),
                                             self.bot.loop)

    def stop(self, ctx):
        self.queue.clear_queue()
        if self.queue.voice_channel.is_playing():
            self.queue.voice_channel.stop()
        elif self.queue.voice_channel.is_paused():
            self.queue.voice_channel.stop()

        self.queue.playing_now_embed = None

    def leave(self, ctx):
        self.pause(ctx)
        asyncio.run_coroutine_threadsafe(self.queue.voice_channel.disconnect(), self.bot.loop)

    def pause(self, ctx):
        if not self.queue.voice_channel.is_paused():
            self.queue.voice_channel.pause()

    def resume(self, ctx):
        if not self.queue.voice_channel.is_playing():
            self.queue.voice_channel.resume()
        elif self.queue.voice_channel.is_playing():
            asyncio.run_coroutine_threadsafe(ctx.send('Not paused!'), self.bot.loop)

    @commands.command(aliases=['play', 'p'])
    async def play_video(self, ctx, *, arg):
        await self.connect(ctx)
        try:
            video = self.extract(arg)
        except IndexError:
            await ctx.send('Song not found.')
            await self.queue.voice_channel.disconnect()
            return

        if not self.queue.voice_channel.is_playing():
            url = self.return_url(video)

            await self.play(ctx, url, video)
        else:
            self.queue.add_track(video)
            await ctx.send(f'{video.get("title")} added to queue.')

    @commands.command(aliases=['skip', 's'])
    async def skip_video(self, ctx):
        try:
            self.skip(ctx)
            await ctx.send('Skipped')
        except AttributeError:
            return

    @commands.command(aliases=['queue', 'q'])
    async def queue_embed(self, ctx):
        now = self.queue.return_playing_now()

        if now is not None:
            embed = discord.Embed(title='Songs in Que:', colour=0xf0cd4f)
            embed.add_field(name='Now playing:', value=now, inline=False)

            for i in range(self.queue.length()):
                video = self.queue.get_by_id(i)
                embed.add_field(name=i + 1, value=video.get('title'), inline=False)

            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(title='Songs in Que', colour=0xf0cd4f, description='Queue is empty.')
            await ctx.send(embed=embed)

    @commands.command(aliases=['leave', 'l'])
    async def leave_channel(self, ctx):
        try:
            self.leave(ctx)
            await ctx.send('Bot has left the channel.')
        except AttributeError:
            return

    @commands.command(aliases=['stop'])
    async def stop_video(self, ctx):
        try:
            self.stop(ctx)
            await ctx.send('Stopped')
        except AttributeError:
            return

    @commands.command(aliases=['pause'])
    async def pause_video(self, ctx):
        try:
            if not self.queue.voice_channel.is_paused():
                self.pause(ctx)
                await ctx.send('Video is paused.')
            else:
                return

        except AttributeError:
            return

    @commands.command(aliases=['resume', 'r'])
    async def resume_video(self, ctx):
        try:
            self.resume(ctx)
            await ctx.send('Resumed')
        except AttributeError:
            return


async def setup(bot):
    await bot.add_cog(YoutubeMusic(bot))
