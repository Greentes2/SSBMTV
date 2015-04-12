# SSBMTV

SSBMTV is a project aiming to provide you with 24h/24 Melee streaming.

It's currently in its very alpha stage, can't be up all the time, and there are several issues with the stream.

That's why you can help me with it!

# How do I use this code?

Simple, just install [willie](https://github.com/embolalia/willie) the bot, then clone this repository into willie (which should be somewhere in the Python libs), and override its files with these files. To run it though, you must change some settings in its configuration files.

# List of bugs to fix ASAP:

* VLC player sometimes "refreshing" the current player's window with a new one. When it happens, OBS loses the focus on the VLC player's window, and if I'm not here to reset it manually, it means a black screen for everyone, which sucks.
  * Some people suggested me to use the MediaListPlayer class of VLC (instead of the MediaPlayer class), but I can't get to work with it. From what I've understood, you can't really get informations about the media being played. Plus, creating a playlist inside of the Python script creates access violations (but it's not a big deal since I can always create the .xpls file manually, it takes like 15 seconds).
  * There might be some hidden super secret option to keep using the MediaPlayer class and not have this annoying window-refreshing thing.
* The VLC player automatically freezes the video in the player when you switch to a full screen application. It might be a Windows-only bug, but whenever I switch to a full screen game, the video just freezes for everyone. So, right now, I just play my games in windowed mode, which sucks for some of them. I think this "bug" might just be an optimization from VLC, just stopping the video rendering because you're full screen anyway, so how could you watch the media anyway?

# Where is the code?

In the root directory, I only changed some code in the bot.py file. Everything's documented, it's in the init function.
Every other changed file should be in the modules directory. There are the core modules of the bot, mainly start, stop, save, rate, getrating, next, voteskip, nowplaying, and help.
