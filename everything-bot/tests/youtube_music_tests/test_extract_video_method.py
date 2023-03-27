import unittest
from unittest.mock import MagicMock
from cogs.youtube_music import YouTubeMusic


class TestYouTubeMusicExtractVideo(unittest.TestCase):
    SEARCH_QUERY = 'back in black'
    VIDEO_URL = 'https://www.youtube.com/watch?v=pAgnJDJN4VA'

    def setUp(self) -> None:
        self.bot = MagicMock()
        self.youtube_music = YouTubeMusic(self.bot)
        self.expected_data = {
            'id': 'pAgnJDJN4VA',
            'title': 'AC/DC - Back In Black (Official Video)',
            'duration': 254,
            'uploader': 'acdcVEVO',
        }

    def test_extract_video_via_search_query(self):
        video = self.youtube_music.extract_video(self.SEARCH_QUERY)

        for k, v in self.expected_data.items():
            self.assertEqual(video[k], v)

    def test_extract_video_via_URL(self):
        video = self.youtube_music.extract_video(self.VIDEO_URL)

        for k, v in self.expected_data.items():
            self.assertEqual(video[k], v)
