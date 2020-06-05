import discord

def return_color_str_to_color_emb(color):
	if color == None:
		return color
	elif color == "":
		return None
	elif color == "discord.Color.teal()":
		return discord.Color.teal()
	elif color == "discord.Color.dark_teal()":
		return discord.Color.dark_teal()
	elif color == "discord.Color.green()":
		return discord.Color.green()
	elif color == "discord.Color.dark_green":
		return discord.Color.dark_green()
	elif color == "discord.Color.blue()":
		return discord.Color.dark_blue()
	elif color == "discord.Color.purple()":
		return discord.Color.purple()
	elif color == "discord.Color.dark_purple()":
		return discord.Color.dark_purple()
	elif color == "discord.Color.magenta()":
		return discord.Color.magenta()
	elif color == "discord.Color.dark_magenta()":
		return discord.Color.dark_magenta()
	elif color == "discord.Color.gold()":
		return discord.Color.gold()
	elif color == "discord.Color.dark_gold()":
		return discord.Color.dark_gold()
	elif color == "discord.Color.orange()":
		return discord.Color.orange()
	elif color == "discord.Color.dark_orange()":
		return discord.Color.dark_orange()
	elif color == "discord.Color.red()":
		return discord.Color.red()
	elif color == "discord.Color.dark_red()":
		return discord.Color.dark_red()
	elif color == "discord.Color.lighter_grey()":
		return discord.Color.lighter_grey()
	elif color == "discord.Color.dark_grey()":
		return discord.Color.dark_grey()
	elif color == "discord.Color.light_grey()":
		return discord.Color.light_grey()
	elif color == "discord.Color.darker_grey()":
		return discord.Color.darker_grey()
	elif color == "discord.Color.blurple()":
		return discord.Color.blurple()
	elif color == "discord.Color.greyple()":
		return discord.Color.greyple()