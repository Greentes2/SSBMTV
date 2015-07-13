import willie.module
import re

@willie.module.commands('nowplaying', 'np')
def nowplaying(bot, trigger):
	"""Gives informations about the video being played."""

        lp_list = {"Apex 2013",
                   "Apex 2014",
                   "APEX 2015",
                   "Avalon IV",
                   "Avalon VI",
                   "B.E.A.S.T 4",
                   "B.E.A.S.T 5",
                   "Beauty10",
                   "BMR",
                   "DYFWI",
                   "Evo 2013",
                   "Evo 2014",
                   "KTAR XI",
                   "NCR2015",
                   "PolyBash XIII",
                   "RoF 3",
                   "Shots Fired",
                   "SSS",
                   "SSS 29",
                   "SSS 30",
                   "WHOBO MLG",
                   "Zenith 2013",
                   "Zenith 2014"}

	reg = re.compile('(.*;){6}.*(;.*)?')
	vid_name = bot.matches_tab[bot.tmp]
	if (reg.match(vid_name)):
		l = vid_name[:-4].split(";")
		tournament = l[0]
                lp_txt = " More information about that event on Liquipedia: "
                lp_link = "http://wiki.teamliquid.net/smash/"
                tournament_url = tournament.replace(" ", "_")
                lp_s = lp_txt + lp_link + tournament_url if tournament in lp_list\
                       else ''
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
Be nice and give the video a like: http://www.youtube.com/watch?v=' + yid + lp_s)
		elif len(l) == 7:
			provider = l[5]
			yid = l[6]
			bot.say("Now playing: " + tournament +\
', ' + p1 + ' (' + char1 + ') VS. ' + p2 + ' (' + char2 + '). \
Thanks to ' + provider + ' for allowing us to stream this video! \
Be nice and give them a like: http://www.youtube.com/watch?v=' + yid + lp_s)
	else:
		bot.say("Now playing: " + vid_name[:-4] + " (unrecognized name format)")
