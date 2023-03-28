import unittest
from unittest.mock import Mock

from cogs.youtube_music import YouTubeMusic, Queue


class TestYouTubeMusicStop(unittest.TestCase):
    def setUp(self):
        self.bot_mock = Mock()
        self.youtube_music = YouTubeMusic(self.bot_mock)
        self.youtube_music.voice_channel = Mock()
        self.youtube_music.queue = Queue()
        self.mock_song = {
            'title': 'Foo'
        }

    def test_stop_clears_queue(self):
        self.youtube_music.queue.add_track(self.mock_song['title'])
        self.youtube_music.queue.add_track('Song 2')
        self.assertEqual(self.youtube_music.queue.length(), 2)
        self.youtube_music.stop(Mock())
        self.assertEqual(self.youtube_music.queue.length(), 0)

    def test_stop_stops_playing(self):
        self.youtube_music.queue.add_track(self.mock_song['title'])
        self.youtube_music.voice_channel.is_playing.return_value = True
        self.youtube_music.stop(Mock())
        self.youtube_music.voice_channel.stop.assert_called_once()

    def test_stop_clears_playing_now(self):
        self.youtube_music.queue.add_track(self.mock_song['title'])
        self.youtube_music.playing_now = self.mock_song
        self.youtube_music.stop(Mock())
        self.assertIsNone(self.youtube_music.playing_now)

    def test_stop_clears_playing_now_embed(self):
        self.youtube_music.voice_channel = Mock()
        self.youtube_music.queue = Queue()
        self.youtube_music.queue.add_track(self.mock_song['title'])
        self.youtube_music.playing_now_embed = Mock()
        self.youtube_music.stop(Mock())
        self.assertIsNone(self.youtube_music.playing_now_embed)
