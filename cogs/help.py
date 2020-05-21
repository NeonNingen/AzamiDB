import discord
from discord.ext import commands

color_list = [discord.Color.red(), discord.Color.green(), discord.Color.blue(),
			  discord.Color.orange(), discord.Color.purple(), discord.Color.gold(),
			  discord.Color.blurple(), discord.Color.greyple(), discord.Color.teal(),
			  discord.Color.dark_red(), discord.Color.dark_green(),
			  discord.Color.light_grey(), discord.Color.dark_gold()]

class Help(commands.Cog):

	def __init__(self, azami):
		self.azami = azami

	'''

	@commands.command(name='help', hidden=True)
	async def help(ctx)

	'''


def setup(azami):
	azami.add_cog(Help(azami))
