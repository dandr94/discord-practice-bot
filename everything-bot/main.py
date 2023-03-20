import os

import discord
from discord.ext import commands

TOKEN = os.getenv('TOKEN')


class Client(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or('!'), intents=discord.Intents.all())
        self.custom_cogs = ['cogs.death_roll_game', 'cogs.youtube_music']

    async def setup_hook(self) -> None:
        for ext in self.custom_cogs:
            await self.load_extension(ext)

    async def on_ready(self):
        print(f'Works!')


def main():
    client = Client()
    client.run(TOKEN)


if __name__ == '__main__':
    main()
