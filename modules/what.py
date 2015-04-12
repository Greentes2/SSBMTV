import willie.module

@willie.module.commands('what')
def what(bot, trigger):
	"""Gives informations about the channel."""
	bot.say("SSBMTV is a webTV for Melee. \
None of the videos streamed here are live, \
it's only rebroadcasting. I asked the content \
creators the right to do so, so just chill, watch, and chat!")