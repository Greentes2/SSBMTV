import willie.module
import json

@willie.module.commands('save')
@willie.module.require_admin("You're not allowed to do that.")
def save(bot, trigger):
	"""Saves stuff"""
	out_file = open("ratings.json", "w")
	json.dump(bot.rates_tab, out_file, indent=2)
	out_file.close()