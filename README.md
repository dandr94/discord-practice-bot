# Discord Bot
This is a Discord bot built using the discord.py library. The bot features a Death Roll game and YouTube music playback functionality.

## Features
## Death Roll Game
The Death Roll game allows players to take turns rolling a number that decreases until someone rolls a 1 and loses the game.

### Commands
**!challenge <player> <start_roll>**: Challenge a player to a new Death Roll game.</br>
**!cancel**: Cancel the current Death Roll game.</br>
**!roll <roll>**: Roll a number to continue the Death Roll game.

## YouTube Music Playback
The bot can play and manage a queue of YouTube music tracks in a voice channel.

### Commands
**!play, !p <song_name/YouTube_URL>**: Play a song or add it to the queue.</br>
**!skip, !s**: Skip the current playing song.</br>
**!queue, !q, !que**: Display the current queue of songs.</br>
**!current, !song**: Show information about the currently playing song.</br>
**!leave, !l**: Make the bot leave the voice channel.</br>
**!stop**: Stop playing and clear the queue.</br>
**!pause**: Pause the current playing song.</br>
**!resume, !r**: Resume playing a paused song.</br>

## Setup and Usage
1. Clone this repository.
2. Install the required dependencies:</br>
```pip install -r requirements.txt```
3. Set up your Discord bot and obtain a token. [Read this for more information](https://discord.com/developers/docs/getting-started)
4. Create a **'.env'** file in the root directory and add your bot token:</br>
```TOKEN=your_bot_token_here```
5. Run the bot:</br>
```python main.py```

## Credits
Discord.py library: [discord.py](https://github.com/Rapptz/discord.py)
yt-dlp library: [yt-dlp](https://github.com/yt-dlp/yt-dlp)