import discord

def color_choice(num):
	color_select = {'1': discord.Color.teal(),
					'2': discord.Color.dark_teal(),
					'3': discord.Color.green(),
					'4': discord.Color.dark_green(),
					'5': discord.Color.dark_blue(),
					'6': discord.Color.purple(),
					'7': discord.Color.dark_purple(),
					'8': discord.Color.magenta(),
					'9': discord.Color.dark_magenta(),
					'10': discord.Color.gold(),
					'11': discord.Color.dark_gold(),
					'12': discord.Color.orange(),
					'13': discord.Color.dark_orange(),
					'14': discord.Color.red(),
					'15': discord.Color.dark_red(),
					'16': discord.Color.lighter_grey(),
					'17': discord.Color.dark_grey(),
					'18': discord.Color.light_grey(),
					'19': discord.Color.darker_grey(),
					'20': discord.Color.blurple(),
					'21': discord.Color.greypie()}
	
	color = color_select[num]
	return color