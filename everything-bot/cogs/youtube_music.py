import datetime
from collections import deque
import discord
import asyncio
from discord.ext import commands
from yt_dlp import YoutubeDL
from cogs.utils import YouTubeMusicUtils


class Queue:
    def __init__(self):
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

    @staticmethod
    def get_title(video):
        return video.get('title')

    @staticmethod
    def get_duration(video):
        return video.get('duration')

    @staticmethod
    def get_youtube_url(video):
        return video.get('webpage_url')

    @staticmethod
    def get_thumbnail(video):
        return video.get('thumbnail')


class YouTubeMusic(commands.Cog, YouTubeMusicUtils):
    """
        A class used to represent an YouTubeMusic player.
        Users can interact with the play using the various commands of the class.

        Available commands:
        -------
        1. !play (song name / YouTube URL) - Available also with !p or !play_video
        Connects the bot to the channel if it's not already in the channel and
        plays the requested song if the Queue is empty, otherwise places the song in the Queue.

        2. !skip - Available also with !skip_video
        Skips the current playing song.

        3. !queue - Available also with !q or !que
        Shows the current songs in the Queue. If it's empty it show 'Queue is empty.'

        4. !leave - Available also with !l or !leave_channel
        Kicks the bot from the current voice channel.

        5. !stop - Available also with !stop_video
        Stops the bot from playing and clears the Queue.
        The bot remains in the channel for further usage.

        6. !pause - Available also with !pause_video
        Pauses the current song.

        7. !resume - Available also with !resume_video
        Resumes the current paused song.

    """

    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot
        self.queue: Queue = Queue()
        self.voice_channel = None

    async def connect(self, ctx):
        """
        Connects the bot to the voice channel that the user who sent the message is currently in.
        """
        try:
            if not ctx.message.author.voice:
                await ctx.send(self.CONNECT_ERROR_MESSAGE)

            vc = ctx.message.author.voice.channel
            self.voice_channel = await vc.connect()
        except:
            pass

    def extract_video(self, arg):
        """
        Method that extracts information about a YouTube video using the provided search query or video ID.
        """
        video = None

        with YoutubeDL(self.YDL_OPTIONS) as ydl:
            try:
                video = ydl.extract_info(f"ytsearch:{arg}", download=False)['entries'][0]
            except:
                video = ydl.extract_info(arg, download=False)

        return video

    @staticmethod
    def return_url(video):
        """
        Method that returns the url of the audio source.
        """
        url = video['url']
        return url

    def construct_queue_embed(self, now_playing):
        """
        The method constructs an embed message containing a list of videos that are in the Queue to be displayed.
        If it's empty returns 'Queue is empty.'
        """
        if now_playing is None or self.queue.is_empty():
            embed = discord.Embed(title=self.EMBED_QUEUE_EMPTY_TITLE, colour=self.EMBED_QUEUE_TITLE_COLOR)
            return embed

        embed = discord.Embed(title=self.EMBED_QUEUE_TITLE, colour=self.EMBED_QUEUE_TITLE_COLOR)

        for i in range(self.queue.length()):
            field_name = f'{i + 1 if i > 0 else "Next"}.'
            video = self.queue.get_by_id(i - 1)
            field_value = self.queue.get_title(video)

            embed.add_field(name=field_name, value=field_value, inline=False)

        return embed

    @staticmethod
    def construct_message_embed(title, description, color):
        """
        Embed message factory method that constructs an embed.
        """

        embed = discord.Embed(title=title,
                              description=description,
                              colour=color)

        return embed

    async def play(self, ctx, url, video):
        """
        The method uses the "play" method of the "voice_channel" object to play audio from the provided "url".
        The method then retrieves information about the video being played.
        Next, the method constructs an embed message to display information about the video being played.

        """
        self.voice_channel.play(
            discord.FFmpegPCMAudio(source=url, **self.FFMPEG_OPTIONS),
        )

        duration = self.queue.get_duration(video)
        title = self.queue.get_title(video)
        youtube_url = self.queue.get_youtube_url(video)
        thumbnail = self.queue.get_thumbnail(video)

        embed = self.construct_message_embed(title=self.EMBED_MESSAGE_TITLE, description=title,
                                             color=self.EMBED_MESSAGE_TITLE_COLOR) \
            .add_field(name=self.EMBED_MESSAGE_DURATION_NAME, value=datetime.timedelta(seconds=duration)) \
            .add_field(name=self.EMBED_MESSAGE_REQUESTED_BY_NAME, value=ctx.author.mention) \
            .add_field(name=self.EMBED_MESSAGE_URL_NAME, value=youtube_url, inline=False) \
            .set_thumbnail(url=thumbnail)

        embed_message = await ctx.send(embed=embed)

        self.queue.playing_now_embed = embed_message

        self.queue.set_playing_now(title)

    def skip(self, ctx):
        """
        Method that handles playing the next track in the queue.
        If there is a song in Queue it retrieves it and plays it. Otherwise, returns "Queue is empty".
        """

        asyncio.run_coroutine_threadsafe(self.queue.playing_now_embed.edit(), self.bot.loop)
        if self.voice_channel.is_playing():
            self.voice_channel.pause()
        if not self.queue.is_empty():
            next_track = self.queue.play_next()
            url = self.return_url(next_track)
            asyncio.run_coroutine_threadsafe(self.play(ctx, url, next_track), self.bot.loop)
            if self.queue.playing_now_embed is not None:
                self.queue.playing_now_embed = None
        else:
            asyncio.run_coroutine_threadsafe(ctx.send(self.EMBED_QUEUE_EMPTY_TITLE, delete_after=3),
                                             self.bot.loop)

    def stop(self, ctx):
        """
        Method that stops the audio and clears the Queue.
        The bot remains in the channel for further usage.
        """
        self.queue.clear_queue()
        if self.voice_channel.is_playing():
            self.voice_channel.stop()
        elif self.voice_channel.is_paused():
            self.voice_channel.stop()

        self.queue.playing_now_embed = None

    def leave(self, ctx):
        """
        Method that pauses the bot and disconnects it from the channel.
        """
        self.pause(ctx)
        asyncio.run_coroutine_threadsafe(self.voice_channel.disconnect(), self.bot.loop)

    def pause(self, ctx):
        """
        Method that pauses the current playing song if song is being played.
        """
        if not self.voice_channel.is_paused():
            self.voice_channel.pause()

    def resume(self, ctx):
        """
        Method that resumes the current paused song. Otherwise, returns 'Not paused.'
        """
        if not self.voice_channel.is_playing():
            self.voice_channel.resume()
        elif self.voice_channel.is_playing():
            asyncio.run_coroutine_threadsafe(ctx.send(self.RESUME_ERROR_MESSAGE), self.bot.loop)

    @commands.command(aliases=['play', 'p'])
    async def play_video(self, ctx, *, arg):
        """
        Command that uses the 'play' method.
        It tries to retrieve the song otherwise, returns 'Song not found.'
        If the song is found and the Queue is empty it plays the song otherwise, adds the song to the Queue.
        """
        await self.connect(ctx)
        try:
            video = self.extract_video(arg)
        except IndexError:
            await ctx.send(self.EXTRACT_ERROR_MESSAGE)
            await self.voice_channel.disconnect()
            return

        if not self.voice_channel.is_playing():
            url = self.return_url(video)

            await self.play(ctx, url, video)
        else:
            self.queue.add_track(video)
            await ctx.send(f'{video.get("title")} added to queue.')

    # Commands
    @commands.command(aliases=['skip', 's'])
    async def skip_video(self, ctx):
        """
        Command that uses the 'skip' method.
        If it is successful it returns 'Skipped'.
        """
        try:
            self.skip(ctx)
            await ctx.send(self.SKIP_MESSAGE)
        except AttributeError:
            return

    @commands.command(aliases=['queue', 'q', 'que'])
    async def show_queue(self, ctx):
        """
        Command uses the 'construct_queue_embed' method.
        Returns an embedded message.
        """
        now_playing = self.queue.return_playing_now()

        embed = self.construct_queue_embed(now_playing)

        await ctx.send(embed=embed)

    @commands.command(aliases=['leave', 'l'])
    async def leave_channel(self, ctx):
        """
        Command that uses the 'leave' method.
        If it is successful it returns a message.
        """
        try:
            self.leave(ctx)
            await ctx.send(self.LEAVE_CHANNEL_MESSAGE)
        except AttributeError:
            return

    @commands.command(aliases=['stop'])
    async def stop_video(self, ctx):
        """
        Command that uses the 'stop' method.
        If it is successful it returns a message.
        """
        try:
            self.stop(ctx)
            await ctx.send(self.STOP_MESSAGE)
        except AttributeError:
            return

    @commands.command(aliases=['pause'])  # Works
    async def pause_video(self, ctx):
        """
        Command that uses the 'pause' method.
        Returns a message if it is successful.
        """
        try:
            if not self.voice_channel.is_paused():
                self.pause(ctx)
                await ctx.send(self.PAUSE_MESSAGE)
            else:
                return

        except AttributeError:
            return

    @commands.command(aliases=['resume', 'r'])
    async def resume_video(self, ctx):
        """
        Command that uses the 'resume' method.
        If it is successful it returns a message.

        """
        try:
            self.resume(ctx)
            await ctx.send(self.RESUME_MESSAGE)
        except AttributeError:
            return


async def setup(bot):
    await bot.add_cog(YouTubeMusic(bot))
