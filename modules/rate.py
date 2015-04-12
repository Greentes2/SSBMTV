import willie.module
import re

@willie.module.commands('rate')
def rate(bot, trigger):
	"""Allows you to rate the video being played, from 0 to 10."""
	vid_name = bot.matches_tab[bot.tmp]
	reg = re.compile('([a-zA-Z0-9-_,.!()& ]+;){6}[a-zA-Z0-9-_,.!()& ]+(;[a-zA-Z0-9-_,.!()& ]+)?')
	if not reg.match(vid_name):
		bot.say("Name format unrecognised. Sorry, I can't let you rate a video like that! \
Head over here to fix that: https://docs.google.com/spreadsheets/d/1pkhEiTmSAUPZ0zEYvjfYRvCakCbB3KJI3-eTcbzCjzs/edit?usp=sharing")
		return

	x = 0
	try:
		x = int(trigger.group(2))
	except ValueError:
		bot.say("!rate must be followed by an integer from 0 to 10.")
		return

	if x < 0 or x > 10:
		bot.say("!rate must be followed by an integer from 0 to 10.")
		return

	nickname = trigger.nick.lower()

	if bot.rates_tab.has_key(vid_name):
		if nickname in [t[0] for t in bot.rates_tab[vid_name]]:
			# Update rating
			bot.say("Found nickname! Updating your rating. Old rating: " + str(t[1]))
			t[1] = x
		else:
			bot.say("Didn't found your nickname, adding it to the list. Thanks for voting! :D")
			bot.rates_tab[vid_name].append([nickname, trigger.group(2)])
	else:
		bot.say("Match not found, adding entry to the dictionary... Thanks for voting! :D")
		tmpdict = {
			vid_name: [[nickname, trigger.group(2)]]
		}
		bot.rates_tab.update(tmpdict)