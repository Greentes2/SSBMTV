import willie.module
from willie.modules.save import save

@willie.module.commands('stop')
@willie.module.require_admin("You're not allowed to do that.")
def stop(bot, trigger):
	"""STOPS EVERYTHING Keepo"""
	save(bot, trigger)
	bot.say("Saved ratings. All clear! Keepo")
	#bot.player.close()