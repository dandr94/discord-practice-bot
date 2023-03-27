import unittest
from unittest.mock import MagicMock

import discord
import datetime

from cogs.youtube_music import YouTubeMusic


class TestYouTubeMusicConstructPlayEmbed(unittest.TestCase):
    def setUp(self) -> None:
        self.bot = MagicMock()
        self.youtube_music = YouTubeMusic(self.bot)

    def test_construct_play_embed(self):
        title = "FooBarBarz"
        duration = 3600  # 1 hour in seconds
        thumbnail = "https://foo.barz/barz.jpg"
        requested_by = "Foo"
        youtube_url = "https://www.youtube.com/watch?v=VIDEO_ID"

        expected_embed = discord.Embed(
            title=self.youtube_music.EMBED_MESSAGE_TITLE,
            description=title,
            color=self.youtube_music.EMBED_MESSAGE_TITLE_COLOR
        )
        expected_embed.add_field(
            name=self.youtube_music.EMBED_MESSAGE_DURATION_NAME,
            value=datetime.timedelta(seconds=duration)
        )
        expected_embed.add_field(
            name=self.youtube_music.EMBED_MESSAGE_REQUESTED_BY_NAME,
            value=requested_by
        )
        expected_embed.add_field(
            name=self.youtube_music.EMBED_MESSAGE_URL_NAME,
            value=youtube_url,
            inline=False
        )
        expected_embed.set_thumbnail(url=thumbnail)

        actual_embed = self.youtube_music.construct_play_embed(title, duration, thumbnail, requested_by, youtube_url)

        self.assertEqual(expected_embed.to_dict(), actual_embed.to_dict())
