import discord
from discord.ext import commands

class Help(commands.Cog):

	def __init__(self, azami):
		self.azami = azami

def setup(azami):
	azami.add_cog(Help(azami))