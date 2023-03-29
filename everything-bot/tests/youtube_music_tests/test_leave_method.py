import unittest
from unittest.mock import MagicMock, Mock

from cogs.youtube_music import YouTubeMusic


class TestYouTubeMusicLeave(unittest.TestCase):
    def setUp(self):
        self.bot_mock = Mock()
        self.youtube_music = YouTubeMusic(self.bot_mock)
        self.voice_channel_mock = MagicMock()
        self.youtube_music.voice_channel = self.voice_channel_mock

    def test_leave(self):
        # Mock the disconnect method of the voice channel to be a coroutine
        async def mock_disconnect():
            pass

        self.voice_channel_mock.disconnect = MagicMock(return_value=mock_disconnect())

        self.youtube_music.leave(Mock())

        self.voice_channel_mock.pause.assert_called_once()

        self.voice_channel_mock.disconnect.assert_called_once()

        self.voice_channel_mock.disconnect.assert_called_with()

    def test_pause(self):
        self.youtube_music.pause(Mock())
        self.voice_channel_mock.pause.assert_called_once()
        self.assertTrue(self.voice_channel_mock.is_paused())
