import discord, os
from discord.ext import commands, tasks
from AzamiDX.core.bot import AzamiBot


def create_bot():
	azami = AzamiBot()
	return azami

def heroku_check():
	try:
		token = os.environ['TOKEN']
		heroku = True
	except KeyError:
		heroku = False

	if heroku == True:
		print("Heroku Detected, Heroku Enabled")
		return token
	else:
		print("Heroku Not-Detected, Commence Local Token")
		token = open("token.txt", "r").read()
		return token

