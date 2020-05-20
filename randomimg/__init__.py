import discord
from random import choice
'''
Try aiohttp when bot reaches 500mb
Make giphy account to store gifs forever
Use this idea:
https://github.com/KingOfPlagues/ViralBot/blob/master/discordbot/utils/util.py
'''
def slap():
	slap_list = [
	'https://media.giphy.com/media/l3vRb8wtvRtW9mOk0/giphy.gif',
	'https://media.giphy.com/media/l1IYa5UYE8iBLWp6E/giphy.gif',
	'https://media0.giphy.com/media/xUPGcF8xjWmt2CRuo0/giphy.gif',
	'https://media1.giphy.com/media/JBsgmn8uGR5hm/giphy.gif'
	]
	return choice(slap_list)

def shoot(num: int):
	if num == 1:
		gif_list = [
			discord.File('./gifs/shoot_gif1.gif'),
			discord.File('./gifs/shoot_gif2.gif')
			]
		return choice(gif_list)
	elif num == 2:
		return discord.File('./gifs/shoot_gif3.gif')
	elif num == 3:
		return discord.File('./gifs/shoot_gif4.gif')


		

	