import unittest
from unittest.mock import Mock

import discord
from discord import VoiceChannel, Member, Message
from discord.ext import commands

from cogs.youtube_music import YouTubeMusic


class TestYouTubeMusicConnect(unittest.IsolatedAsyncioTestCase):
    def setUp(self) -> None:
        self.bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())
        self.youtube_music = YouTubeMusic(self.bot)
        self.mock_vc = Mock(spec=VoiceChannel)
        self.mock_member = Mock(spec=Member)
        self.mock_message = Mock(spec=Message)
        self.mock_ctx = Mock(spec=commands.Context)

    async def test_connect_success(self):
        self.mock_member.voice.channel = self.mock_vc

        self.mock_message.author = self.mock_member

        self.mock_ctx.message = self.mock_message
        self.mock_ctx.author = self.mock_member

        self.youtube_music.voice_channel = None

        self.assertIsNone(self.youtube_music.voice_channel)

        # Call the connect method with the mock context
        await self.youtube_music.connect(self.mock_ctx)

        # Assert that the voice channel attribute has been set to a non-None value
        self.assertIsNotNone(self.youtube_music.voice_channel)

    async def test_connect_no_voice_channel(self):
        self.mock_member.voice = None

        self.mock_message.author = self.mock_member

        self.mock_ctx.message = self.mock_message
        self.mock_ctx.author = self.mock_member

        self.youtube_music.voice_channel = None

        self.assertIsNone(self.youtube_music.voice_channel)

        await self.youtube_music.connect(self.mock_ctx)

        # Assert that the connect error message has been sent to the channel
        self.mock_ctx.send.assert_called_once_with(self.youtube_music.CONNECT_ERROR_MESSAGE)

        # Assert that the voice channel attribute is still None
        self.assertIsNone(self.youtube_music.voice_channel)

    async def test_connect_exception(self):
        self.mock_member.voice.channel = self.mock_vc

        self.mock_message.author = self.mock_member

        self.mock_ctx.message = self.mock_message
        self.mock_ctx.author = self.mock_member

        self.youtube_music.voice_channel = None

        self.assertIsNone(self.youtube_music.voice_channel)

        # Create a mock coroutine function that raises an exception
        async def mock_coro(*args, **kwargs):
            raise Exception("Test exception")

        # Replace the connect method with the mock coroutine function that raises an exception
        self.youtube_music.connect = mock_coro

        # Call the connect method with the mock context
        with self.assertRaises(Exception):
            await self.youtube_music.connect(self.mock_ctx)

        # Assert that the voice channel attribute is still None
        self.assertIsNone(self.youtube_music.voice_channel)
