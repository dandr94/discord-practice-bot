import discord


def construct_message_embed(title, description, color):
    """
    Embed message factory method that constructs an embed.
    """

    embed = discord.Embed(title=title,
                          description=description,
                          colour=color)

    return embed


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
    ADD_TO_QUEUE_MESSAGE = ' added to queue.'

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

    @staticmethod
    def get_video_source(video):
        return video.get('url')


class HelpUtils:
    EMBED_TITLE_COLOR = 0xff2a2a
    EMBED_ADD_FIELD_EXAMPLE_NAME = 'Example:'
    EMBED_ADD_FIELD_COMMANDS_NAME = 'Commands:'

    # GLOBAL HELP
    GLOBAL_EMBED_TITLE = 'Everything Bot'
    GLOBAL_EMBED_DESCRIPTION = 'Available commands:'
    CMDS_LIST = ['!help deathroll', '!help youtubemusic']
    CMD_HELP_TEXT = 'Shows the current available commands for '

    # DEATHROLL HELP
    DEATHROLL_EMBED_TITLE = 'DeathRoll'
    DEATHROLL_EMBED_DESCRIPTION = 'Represents a game of Death Roll, where players take turns rolling a number that is ' \
                                  'decreasing until  someone rolls a 1 and loses the game.'
    DEATHROLL_EMBED_ADD_FIELD_COMMANDS_VALUE = '**!challenge** __(username)__ __(number)__\n' \
                                               '**!roll** __(number)__\n ' \
                                               '**!cancel**'
    DEATHROLL_EMBED_SET_FOOTER_TEXT = 'For more information type !help deathroll (command). Example !help deathroll ' \
                                      'challenge'

    # DEATHROLL CHALLENGE HELP
    CHALLENGE_EMBED_TITLE = '!challenge'
    CHALLENGE_EMBED_DESCRIPTION = 'Challenges a discord member to a new deathroll game. Only one game can be played ' \
                                  'at the time.\nTakes 2 parameters:'
    CHALLENGE_EMBED_ADD_FIELD_USERNAME_NAME = '1. Username'
    CHALLENGE_EMBED_ADD_FIELD_USERNAME_VALUE = 'Type the username of a discord member. Keep in minda that it is case ' \
                                               'sensitive'
    CHALLENGE_EMBED_ADD_FIELD_NUMBER_NAME = '2. Number'
    CHALLENGE_EMBED_ADD_FIELD_NUMBER_VALUE = 'Type the number that you want the deathroll to start from.'
    CHALLENGE_EMBED_ADD_FIELD_EXAMPLE_VALUE = '!challenge Foobarbarz 100'
    CHALLENGE_EMBED_SET_FOOTER_TEXT = 'This will challenge Foobarbarz member to a deathroll game with starting number ' \
                                      'of 100'

    # DEATHROLL ROLL HELP
    ROLL_EMBED_TITLE = '!roll'
    ROLL_EMBED_DESCRIPTION = 'Rolls a number between the last rolled or starting number and 1.\nTakes 1 parameters:'
    ROLL_EMBED_ADD_FIELD_NUMBER_NAME = '1. Number'
    ROLL_EMBED_ADD_FIELD_NUMBER_VALUE = 'Type the last rolled number.'
    ROLL_EMBED_ADD_FIELD_EXAMPLE_VALUE = '!roll 37'
    ROLL_EMBED_SET_FOOTER_TEXT = 'This will roll a number between 1 and 37 inclusive.'

    # DEATHROLL CANCEL HELP
    CANCEL_EMBED_TITLE = '!cancel'
    CANCEL_EMBED_DESCRIPTION = 'Cancels the current on going game.'
    CANCEL_EMBED_ADD_FIELD_EXAMPLE_VALUE = '!cancel'
    CANCEL_EMBED_SET_FOOTER_TEXT = 'This will cancel the game and result in no winner.'

    # YOUTUBEMUSIC HELP
    YOUTUBEMUSIC_EMBED_TITLE = 'YouTube Music'
    YOUTUBEMUSIC_EMBED_DESCRIPTION = 'Represents a YouTube Music player that allows members to request songs to be ' \
                                     'played.'
    YOUTUBEMUSIC_EMBED_ADD_FIELD_COMMANDS_VALUE = '**!play !p** __(Song name/YouTube URL)__\n' \
                                                  f'**!skip !s**\n ' \
                                                  f'**!queue !q !que**\n' \
                                                  f'**!current !song**\n' \
                                                  f'**!leave/!l**\n' \
                                                  f'**!stop**\n' \
                                                  f'**!pause**\n' \
                                                  f'**!resume**'
    YOUTUBEMUSIC_EMBED_SET_FOOTER_TEXT = 'For more information type !help youtubemusic (command). Example !help ' \
                                         'youtubemusic play'

    # YOUTUBEMUSIC PLAY HELP
    PLAY_EMBED_TITLE = '!play'
    PLAY_EMBED_DESCRIPTION = 'Plays the requested song if the Queue is empty. Otherwise, it will place the song ' \
                             'in the Queue.\nTakes 1 parameters:'
    PLAY_EMBED_ADD_FIELD_SONG_URL_NAME = '1. Song name OR YouTube URL'
    PLAY_EMBED_ADD_FIELD_SONG_URL_VALUE = 'Type the song name or the URL of the song. If it is song name it will play ' \
                                          'the first result of the YouTube search result. So if it is a famous song ' \
                                          'you do not even need to provide full information about the song. Example I ' \
                                          'can request only "back in black" and it will play the song by AC/DC ' \
                                          'without me providing the artist name.'
    PLAY_EMBED_ADD_FIELD_EXAMPLE_VALUE = '!play sub focus - solar system'
    PLAY_EMBED_SET_FOOTER_TEXT = 'This will play the song from Sub Focus - Solar System.'

    # YOUTUBEMUSIC SKIP HELP
    SKIP_EMBED_TITLE = '!skip'
    SKIP_EMBED_DESCRIPTION = 'Skips the current playing song.'
    SKIP_EMBED_ADD_FIELD_EXAMPLE_VALUE = '!skip'
    SKIP_EMBED_SET_FOOTER_TEXT = 'This will skip the current song and play the next song from the Queue if it is not ' \
                                 'empty.'

    # YOUTUBEMUSIC QUEUE HELP
    QUEUE_EMBED_TITLE = '!queue'
    QUEUE_EMBED_DESCRIPTION = 'Shows the songs in the Queue'
    QUEUE_EMBED_ADD_FIELD_EXAMPLE_VALUE = '!queue'
    QUEUE_EMBED_SET_FOOTER_TEXT = 'This will show all the songs in the Queue if there are any.'

    # YOUTUBEMUSIC CURRENT HELP
    CURRENT_EMBED_TITLE = '!current'
    CURRENT_EMBED_DESCRIPTION = 'Shows information about the current song.'
    CURRENT_EMBED_ADD_FIELD_EXAMPLE_VALUE = '!current'
    CURRENT_EMBED_SET_FOOTER_TEXT = 'This will show information about the current song. Title, Duration, Requested by ' \
                                    'and URL.'

    # YOUTUBEMUSIC LEAVE HELP
    LEAVE_EMBED_TITLE = '!leave'
    LEAVE_EMBED_DESCRIPTION = 'Kicks the bot from the channel.'
    LEAVE_EMBED_ADD_FIELD_EXAMPLE_VALUE = '!leave'
    LEAVE_EMBED_SET_FOOTER_TEXT = 'This will remove the bot from the voice channel and empty the Queue.'

    # YOUTUBEMUSIC STOP HELP
    STOP_EMBED_TITLE = '!stop'
    STOP_EMBED_DESCRIPTION = 'Stops the bot from playing anymore. It will clear the Queue so if you want to just stop ' \
                             'the bot from playing and the Queue to remain use !pause'
    STOP_EMBED_ADD_FIELD_EXAMPLE_VALUE = '!stop'
    STOP_EMBED_SET_FOOTER_TEXT = 'This will stop the bot from playing and clear the Queue but the bot will remain in ' \
                                 'the channel for further use.'

    # YOUTUBEMUSIC PAUSE HELP
    PAUSE_EMBED_TITLE = '!pause'
    PAUSE_EMBED_DESCRIPTION = 'Pauses the current playing song.'
    PAUSE_EMBED_ADD_FIELD_EXAMPLE_VALUE = '!pause'
    PAUSE_EMBED_SET_FOOTER_TEXT = 'This will pause the current song. You can use !resume to continue playing the ' \
                                  'remaining duration of the song.'

    # YOUTUBEMUSIC RESUME HELP
    RESUME_EMBED_TITLE = '!resume'
    RESUME_EMBED_DESCRIPTION = 'Resumes the current paused song.'
    RESUME_EMBED_ADD_FIELD_EXAMPLE_VALUE = '!resume'
    RESUME_EMBED_SET_FOOTER_TEXT = 'This will resume the current paused song.'
