import willie.module
from willie.modules.next import next

@willie.module.commands('voteskip', 'vs')
def voteskip(bot, trigger):
	"""Starts a skip vote, or votes for the current skip vote."""
	if not trigger.nick in bot.voters:
		if bot.voteskip == 0:
			bot.say("Starting a skip vote. Type !voteskip or !vs to vote to skip the current video.")
			bot.voteskip = bot.voteskip + 1
			bot.voters.append(trigger.nick)
			bot.say(trigger.nick + " voted for the skip!")
		elif bot.voteskip >= 6:
			bot.say(trigger.nick + " voted for the skip! Vote succesful, skipping the current video!")
			next(bot, None)
		else:
			bot.voteskip = bot.voteskip + 1
			bot.voters.append(trigger.nick)
			bot.say(trigger.nick + " voted for the skip!")