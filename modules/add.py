import willie.module

@willie.module.commands('add')
def add(bot, trigger):
	"""Allow you to send me videos you\'d like to see in the playlist. \
Expected format: \
"tournament;first player;his/her character(s);second player;his/her character(s);[moment in the tournament;]YT channel;YT id". \
The moment is optionnal, that\'s why it\'s between brackets! \
The YT id is the 11 characters after "watch?v=" in the YouTube\'s video url."""
	s = trigger.group(2)
	s = s.split(";")
	if len(s) < 7 or len(s) > 8:
		bot.say('Wrong argument. Expected string: \
"tournament;first player;his character(s);second player;his character(s);[moment in the tournament;]YT channel;YT id". \
Please check what you wrote and try again. Also, the moment is optionnal, that\'s why it\'s between brackets! \
The YT id is the 11 characters after "watch?v=" in the YouTube\'s video url.')
	else:
		f = open('add.txt', 'a')
		f.write(trigger.group(2) + '\n')
		f.close()
		bot.say('Video sent to the confirmation list, \
thanks for taking the time to do it right! :D')