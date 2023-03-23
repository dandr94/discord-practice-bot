from discord.ext import commands
from cogs.utils import HelpUtils, construct_message_embed


class Help(commands.Cog, HelpUtils):
    """
        The Help class provides information about the commands of the other cogs.
    """

    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot
        bot.remove_command('help')

    @commands.group(invoke_without_command=True)
    async def help(self, ctx):

        embed = construct_message_embed(title=self.GLOBAL_EMBED_TITLE, description=self.GLOBAL_EMBED_DESCRIPTION,
                                        color=self.EMBED_TITLE_COLOR)
        for cmd in self.CMDS_LIST:
            embed.add_field(name=cmd, value=self.CMD_HELP_TEXT + cmd, inline=False)

        await ctx.send(embed=embed)

    @help.command()
    async def deathroll(self, ctx, arg=None):
        if arg:
            match arg:
                case 'challenge':
                    embed = construct_message_embed(title=self.CHALLENGE_EMBED_TITLE,
                                                    description=self.CHALLENGE_EMBED_DESCRIPTION,
                                                    color=self.EMBED_TITLE_COLOR)
                    embed.add_field(name=self.CHALLENGE_EMBED_ADD_FIELD_USERNAME_NAME,
                                    value=self.CHALLENGE_EMBED_ADD_FIELD_USERNAME_VALUE,
                                    inline=False)
                    embed.add_field(name=self.CHALLENGE_EMBED_ADD_FIELD_NUMBER_NAME,
                                    value=self.CHALLENGE_EMBED_ADD_FIELD_NUMBER_VALUE,
                                    inline=False)
                    embed.add_field(name=self.EMBED_ADD_FIELD_EXAMPLE_NAME,
                                    value=self.CHALLENGE_EMBED_ADD_FIELD_EXAMPLE_VALUE,
                                    inline=False)
                    embed.set_footer(text=self.CHALLENGE_EMBED_SET_FOOTER_TEXT)

                    await ctx.send(embed=embed)
                case 'roll':

                    embed = construct_message_embed(title=self.ROLL_EMBED_TITLE,
                                                    description=self.ROLL_EMBED_DESCRIPTION,
                                                    color=self.EMBED_TITLE_COLOR)
                    embed.add_field(name=self.ROLL_EMBED_ADD_FIELD_NUMBER_NAME,
                                    value=self.ROLL_EMBED_ADD_FIELD_NUMBER_VALUE,
                                    inline=False)
                    embed.add_field(name=self.EMBED_ADD_FIELD_EXAMPLE_NAME,
                                    value=self.ROLL_EMBED_ADD_FIELD_EXAMPLE_VALUE,
                                    inline=False)
                    embed.set_footer(text=self.ROLL_EMBED_SET_FOOTER_TEXT)

                    await ctx.send(embed=embed)
                case 'cancel':

                    embed = construct_message_embed(title=self.CANCEL_EMBED_TITLE,
                                                    description=self.CANCEL_EMBED_DESCRIPTION,
                                                    color=self.EMBED_TITLE_COLOR)
                    embed.add_field(name=self.EMBED_ADD_FIELD_EXAMPLE_NAME,
                                    value=self.CANCEL_EMBED_ADD_FIELD_EXAMPLE_VALUE,
                                    inline=False)
                    embed.set_footer(text=self.CANCEL_EMBED_SET_FOOTER_TEXT)

                    await ctx.send(embed=embed)
        else:
            embed = construct_message_embed(title=self.DEATHROLL_EMBED_TITLE,
                                            description=self.DEATHROLL_EMBED_DESCRIPTION,
                                            color=self.EMBED_TITLE_COLOR)
            embed.add_field(name=self.EMBED_ADD_FIELD_COMMANDS_NAME,
                            value=self.DEATHROLL_EMBED_ADD_FIELD_COMMANDS_VALUE,
                            inline=False)
            embed.set_footer(text=self.DEATHROLL_EMBED_SET_FOOTER_TEXT)

            await ctx.send(embed=embed)

    @help.command()
    async def youtubemusic(self, ctx, arg=None):
        if arg:
            if arg == 'play' or arg == 'p':
                embed = construct_message_embed(title=self.PLAY_EMBED_TITLE,
                                                description=self.PLAY_EMBED_DESCRIPTION,
                                                color=self.EMBED_TITLE_COLOR)
                embed.add_field(name=self.PLAY_EMBED_ADD_FIELD_SONG_URL_NAME,
                                value=self.PLAY_EMBED_ADD_FIELD_SONG_URL_VALUE,
                                inline=False)
                embed.add_field(name=self.EMBED_ADD_FIELD_EXAMPLE_NAME,
                                value=self.PLAY_EMBED_ADD_FIELD_EXAMPLE_VALUE,
                                inline=False)
                embed.set_footer(text=self.PLAY_EMBED_SET_FOOTER_TEXT)

                await ctx.send(embed=embed)

            elif arg == 'skip' or arg == 's':
                embed = construct_message_embed(title=self.SKIP_EMBED_TITLE,
                                                description=self.SKIP_EMBED_DESCRIPTION,
                                                color=self.EMBED_TITLE_COLOR)
                embed.add_field(name=self.EMBED_ADD_FIELD_EXAMPLE_NAME,
                                value=self.SKIP_EMBED_ADD_FIELD_EXAMPLE_VALUE,
                                inline=False)
                embed.set_footer(text=self.SKIP_EMBED_SET_FOOTER_TEXT)

                await ctx.send(embed=embed)

            elif arg == 'queue' or arg == 'que' or arg == 'q':
                embed = construct_message_embed(title=self.QUEUE_EMBED_TITLE,
                                                description=self.QUEUE_EMBED_DESCRIPTION,
                                                color=self.EMBED_TITLE_COLOR)
                embed.add_field(name=self.EMBED_ADD_FIELD_EXAMPLE_NAME,
                                value=self.QUEUE_EMBED_ADD_FIELD_EXAMPLE_VALUE,
                                inline=False)
                embed.set_footer(text=self.QUEUE_EMBED_SET_FOOTER_TEXT)

                await ctx.send(embed=embed)

            elif arg == 'current' or arg == 'song':
                embed = construct_message_embed(title=self.CURRENT_EMBED_TITLE,
                                                description=self.CURRENT_EMBED_DESCRIPTION,
                                                color=self.EMBED_TITLE_COLOR)
                embed.add_field(name=self.EMBED_ADD_FIELD_EXAMPLE_NAME,
                                value=self.CURRENT_EMBED_ADD_FIELD_EXAMPLE_VALUE,
                                inline=False)
                embed.set_footer(text=self.CURRENT_EMBED_SET_FOOTER_TEXT)

                await ctx.send(embed=embed)

            elif arg == 'leave' or arg == 'l':
                embed = construct_message_embed(title=self.LEAVE_EMBED_TITLE,
                                                description=self.LEAVE_EMBED_DESCRIPTION,
                                                color=self.EMBED_TITLE_COLOR)
                embed.add_field(name=self.EMBED_ADD_FIELD_EXAMPLE_NAME,
                                value=self.LEAVE_EMBED_ADD_FIELD_EXAMPLE_VALUE,
                                inline=False)
                embed.set_footer(text=self.LEAVE_EMBED_SET_FOOTER_TEXT)

                await ctx.send(embed=embed)

            elif arg == 'stop':
                embed = construct_message_embed(title=self.STOP_EMBED_TITLE,
                                                description=self.STOP_EMBED_DESCRIPTION,
                                                color=self.EMBED_TITLE_COLOR)
                embed.add_field(name=self.EMBED_ADD_FIELD_EXAMPLE_NAME,
                                value=self.STOP_EMBED_ADD_FIELD_EXAMPLE_VALUE,
                                inline=False)
                embed.set_footer(text=self.STOP_EMBED_SET_FOOTER_TEXT)

                await ctx.send(embed=embed)

            elif arg == 'pause':
                embed = construct_message_embed(title=self.PAUSE_EMBED_TITLE,
                                                description=self.PAUSE_EMBED_DESCRIPTION,
                                                color=self.EMBED_TITLE_COLOR)
                embed.add_field(name=self.EMBED_ADD_FIELD_EXAMPLE_NAME,
                                value=self.PAUSE_EMBED_ADD_FIELD_EXAMPLE_VALUE,
                                inline=False)
                embed.set_footer(text=self.PAUSE_EMBED_SET_FOOTER_TEXT)

                await ctx.send(embed=embed)

            elif arg == 'resume':
                embed = construct_message_embed(title=self.RESUME_EMBED_TITLE,
                                                description=self.RESUME_EMBED_DESCRIPTION,
                                                color=self.EMBED_TITLE_COLOR)
                embed.add_field(name=self.EMBED_ADD_FIELD_EXAMPLE_NAME,
                                value=self.RESUME_EMBED_ADD_FIELD_EXAMPLE_VALUE,
                                inline=False)
                embed.set_footer(text=self.RESUME_EMBED_SET_FOOTER_TEXT)

                await ctx.send(embed=embed)
        else:
            embed = construct_message_embed(title=self.YOUTUBEMUSIC_EMBED_TITLE,
                                            description=self.YOUTUBEMUSIC_EMBED_DESCRIPTION,
                                            color=self.EMBED_TITLE_COLOR)
            embed.add_field(name=self.EMBED_ADD_FIELD_COMMANDS_NAME,
                            value=self.YOUTUBEMUSIC_EMBED_ADD_FIELD_COMMANDS_VALUE,
                            inline=False)
            embed.set_footer(text=self.YOUTUBEMUSIC_EMBED_SET_FOOTER_TEXT)

            await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Help(bot))
