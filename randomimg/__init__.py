import discord
from random import choice

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
			discord.File('gifs/shoot_gif1'),
			discord.File('gifs/shoot_gif2')
			]
		return choice(gif_list)
	elif num == 2:
		return discord.File('gifs/shoot_gif3')
	elif num == 3:
		return discord.File('gifs/shoot_gif4')


		

	