import willie.module
from willie.modules.next import next
import json
from time import sleep

@willie.module.commands('start')
@willie.module.require_admin("You're not allowed to do that.")
def start(bot, trigger):
	next(bot, trigger)
	while True:
		if bot.player.get_state() == 6:
		    next(bot, trigger)