import willie.module
import random
from willie.modules.nowplaying import nowplaying

@willie.module.commands('next', 'n')
def next(bot, trigger):
	if trigger is None or trigger.nick == "ssbmtv":
		bot.tmp = bot.tmp + 1
		if (bot.tmp >= len(bot.matches_tab)):
			bot.tmp = 0
			random.shuffle(bot.matches_tab)
		bot.media = bot.vlc_instance.media_new("Matches\\" \
			+ bot.matches_tab[bot.tmp])
		bot.player.set_media(bot.media)
		bot.player.set_fullscreen(True)
		bot.player.play()
		bot.voteskip = 0
		bot.voters = []
		nowplaying(bot, trigger)