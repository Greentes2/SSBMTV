import willie.module
import random

@willie.module.commands('eyebleach')
def start(bot, trigger):
	bot.say(bot.praw_r.get_random_submission(subreddit='aww').url)