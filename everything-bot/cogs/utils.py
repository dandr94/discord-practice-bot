class YouTubeMusicUtils:
    # YOUTUBEDL OPTIONS
    YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist': 'True', 'quiet': True}

    # FFMPEG OPTIONS
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    FFMPEG_PATH = {'linux': 'ffmpeg'}

    # CONNECT
    CONNECT_ERROR_MESSAGE = 'There was a problem with the connection!'

    # EMBED MESSAGE
    EMBED_MESSAGE_TITLE = 'Now Playing:'
    EMBED_MESSAGE_TITLE_COLOR = 0xff2a2a
    EMBED_MESSAGE_DURATION_NAME = 'Duration:'
    EMBED_MESSAGE_REQUESTED_BY_NAME = 'Requested by:'
    EMBED_MESSAGE_URL_NAME = 'URL:'

    # EMBED QUEUE
    EMBED_QUEUE_TITLE = 'Songs in the queue:'
    EMBED_QUEUE_TITLE_COLOR = 0xf0cd4f
    EMBED_QUEUE_EMPTY_TITLE = 'Queue is empty.'

    # CURRENT_PLAYING_SONG
    CURRENT_PLAYING_SONG_ERROR_MSG = 'There is no current playing song!'

    # QUEUE
    ADD_TO_QUEUE_MESSAGE = 'added to queue.'

    # EXTRACT
    EXTRACT_ERROR_MESSAGE = 'Song not found.'

    # SKIP
    SKIP_MESSAGE = 'Skipped >> '

    # LEAVE
    LEAVE_CHANNEL_MESSAGE = 'Bot has left the channel.'

    # STOP
    STOP_MESSAGE = 'Stopped.'

    # PAUSE
    PAUSE_MESSAGE = 'Paused.'

    # RESUME
    RESUME_MESSAGE = 'Resumed.'
    RESUME_ERROR_MESSAGE = 'Not paused!'

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
