import willie.module
import re

@willie.module.commands('nowplaying', 'np')
def nowplaying(bot, trigger):
	"""Gives informations about the video being played."""
	reg = re.compile('(.*;){6}.*(;.*)?')
	vid_name = bot.matches_tab[bot.tmp]
	if (reg.match(vid_name)):
		l = vid_name[:-4].split(";")
		tournament = l[0]
		p1 = l[1]
		char1 = l[2]
		p2 = l[3]
		char2 = l[4]
		if len(l) == 8:
			moment = l[5]
			provider = l[6]
			yid = l[7]
			bot.say("Now playing: " + tournament + ', ' + moment +\
', ' + p1 + ' (' + char1 + ') VS. ' + p2 + ' (' + char2 + '). \
Thanks to ' + provider + ' for allowing us to stream this video! \
Be nice and give the video a like: http://www.youtube.com/watch?v=' + yid)
		elif len(l) == 7:
			provider = l[5]
			yid = l[6]
			bot.say("Now playing: " + tournament +\
', ' + p1 + ' (' + char1 + ') VS. ' + p2 + ' (' + char2 + '). \
Thanks to ' + provider + ' for allowing us to stream this video! \
Be nice and give them a like: http://www.youtube.com/watch?v=' + yid)
	else:
		bot.say("Now playing: " + vid_name[:-4] + " (unrecognized name format)")