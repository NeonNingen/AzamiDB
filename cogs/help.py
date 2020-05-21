import discord, random
from discord.ext import commands

color_list = [discord.Color.blue(), discord.Color.green()]

class Help(commands.Cog):

	def __init__(self, azami):
		self.azami = azami

	'''

	@commands.command(name="help", description="The help command!", 
					  usage="cog")
	async def help(self, ctx, cog="all"):
		help_embed = discord.Embed(
			title="Help",
			color=)

	'''



def setup(azami):
	azami.add_cog(Help(azami))