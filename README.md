# Discord Bot
This is a Discord bot built using the discord.py library. The bot features a Death Roll game and YouTube music playback functionality.</br>
>*_Tests not fully implemented._*
## Features
## Death Roll Game
The Death Roll game allows players to take turns rolling a number that decreases until someone rolls a 1 and loses the game.

### Commands
- `!challenge` **>player<** **>start_roll<**: Challenge a player to a new Death Roll game.</br>
- `!cancel`: Cancel the current Death Roll game.</br>
- `!roll` <roll>: Roll a number to continue the Death Roll game.

## YouTube Music Playback
The bot can play and manage a queue of YouTube music tracks in a voice channel.

### Commands
- `!play`, `!p` **<u>song_name/YouTube_URL</u>**: Play a song or add it to the queue.</br>
- `!skip`, `!s`: Skip the current playing song.</br>
- `!queue`, `!q`, `!que`: Display the current queue of songs.</br>
- `!current`, `!song`: Show information about the currently playing song.</br>
- `!leave`, `!l`: Make the bot leave the voice channel.</br>
- `!stop`: Stop playing and clear the queue.</br>
- `!pause`: Pause the current playing song.</br>
- `!resume`, `!r`: Resume playing a paused song.</br>

## Help cog
The bot includes a `Help` cog that provides assistance to users in understanding and utilizing the available commands. The `Help` cog supports the following commands:

### Commands

- `!help`: Display information about available commands and their usages.
- `!help deathroll`: Get information about the Death Roll game commands.
- `!help youtubemusic`: Get information about the YouTube Music Playback commands.
- `!help deathroll [subcommand]`: Get information about the Death Roll game subcommands.
- `!help youtubemusic [subcommand]`: Get information about the YouTube Music Playback subcommands.




## Setup and Usage
1. Clone this repository.
2. Go to the root directory:
```bash
cd discord-practice-bot/everything-bot/
```
3. Install the required dependencies:</br>
```bash
pip install -r requirements.txt
```
4. Set up your Discord bot and obtain a token. [Read this for more information](https://discord.com/developers/docs/getting-started).
5. Create a `.env` and add the following environment variable to your `.env`:</br>
`TOKEN=your_discord_token_here`
6. Run the bot:</br>
```bash
python main.py
```

## Credits
1. Discord.py library: [discord.py](https://github.com/Rapptz/discord.py)
2. yt-dlp library: [yt-dlp](https://github.com/yt-dlp/yt-dlp)