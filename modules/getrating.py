import willie.module

@willie.module.commands('getrating')
def getrating(bot, trigger):
	"""Gives you the rating of the video being played."""
	if bot.rates_tab.has_key(bot.matches_tab[bot.tmp]):
		n = 0
		v = 0
		for rate in bot.rates_tab[bot.matches_tab[bot.tmp]]:
			n = n + 1
			v = v + int(rate[1])
		result = v / float(n)
		bot.say("This video has a rating of " + "{:3.1f}".format(result) + ".")
	else:
		bot.say("This video hasn't been rated yet, sorry!")