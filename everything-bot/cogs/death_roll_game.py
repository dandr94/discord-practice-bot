import discord
from discord.ext import commands
from random import randint
from typing import Union


class DeathRoll(commands.Cog):
    """
    Represents a game of Death Roll, where players take turns rolling a number that is decreasing until someone rolls
    a 1 and loses the game.
    """

    def __init__(self, bot: commands.Bot):
        self.bot: commands.Bot = bot
        self.current_player: Union[None, str] = None
        self.other_player: Union[None, str] = None
        self.current_roll: Union[None, int] = None
        self.game_in_progress: bool = False

    @commands.command()
    async def challenge(self, ctx: commands.Context, player: discord.Member, start_roll: int) -> None:

        """Challenge a player to a new death roll game."""

        if self.current_player is not None:
            await ctx.send(
                f"A game is already in progress between {self.current_player.mention} and {self.other_player.mention}.")
        elif player.bot:
            await ctx.send("You cannot play against a bot.")
        else:
            self.current_player = ctx.author
            self.other_player = player
            self.current_roll = start_roll
            self.game_in_progress = True
            await ctx.send(
                f"{self.current_player.mention} challenges {self.other_player.mention} to a death roll game with a "
                f"starting roll of {self.current_roll}."
                f"{self.current_player.mention}, type !roll {self.current_roll} to start the game or !cancel to cancel "
                f"the game.")

    @challenge.error
    async def challenge_errors(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f'{ctx.author.mention}, please provide a number to roll')
        elif isinstance(error, commands.MemberNotFound):
            msg = ctx.message.clean_content.split()[1:][0]
            await ctx.send(f'{msg} is not a member!')

    @commands.command()
    async def cancel(self, ctx: commands.Context) -> None:

        """Cancel the current death roll game."""

        if self.game_in_progress:
            self.current_player = None
            self.other_player = None
            self.current_roll = None
            self.game_in_progress = False
            await ctx.send('Death roll game cancelled.')
        else:
            await ctx.send('There is no death roll game in progress.')

    @commands.command()
    async def roll(self, ctx: commands.Context, roll: int) -> None:

        """Roll a number to continue the death roll game."""

        roll = int(roll)

        if not self.game_in_progress:
            await ctx.send('Death roll game is not yet started! Type !challenge (user) (start roll) to ' \
                           'start a game.')
        elif ctx.author != self.current_player:
            await ctx.send(f"{ctx.author.mention}, it's not your turn to roll!")
        elif roll != self.current_roll:
            await ctx.send(f'{self.current_player.mention} wrong input! Please type !roll {self.current_roll}')
        else:
            self.current_roll = randint(1, roll)

            if self.current_roll == 1:
                await ctx.send(
                    f'{self.current_player.mention} rolls a 1 and loses the game! Better luck next time, {self.current_player.mention}!')
                await self.cancel(ctx)
            else:
                await ctx.send(
                    f'{self.current_player.mention} rolls {self.current_roll}! Your turn {self.other_player.mention}!')
                self.current_player, self.other_player = self.other_player, self.current_player

    @roll.error
    async def roll_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(f"{ctx.author.mention}, please provide a number to roll.")
        if isinstance(error, commands.BadArgument):
            await ctx.send(f"{ctx.author.mention}, please provide a number to roll.")


async def setup(bot):
    await bot.add_cog(DeathRoll(bot))
