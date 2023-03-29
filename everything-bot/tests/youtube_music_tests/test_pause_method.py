import unittest
from unittest.mock import Mock, MagicMock

from cogs.youtube_music import YouTubeMusic


class TestYouTubeMusicPause(unittest.TestCase):
    def setUp(self):
        self.bot_mock = Mock()
        self.youtube_music = YouTubeMusic(self.bot_mock)
        self.voice_channel_mock = MagicMock()
        self.youtube_music.voice_channel = self.voice_channel_mock

    def test_pause(self):
        self.youtube_music.pause(Mock())
        self.voice_channel_mock.pause.assert_called_once()
        self.assertTrue(self.voice_channel_mock.is_paused())

