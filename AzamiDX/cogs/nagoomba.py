import random
from discord.ext import commands
from AzamiDX.etc.img import display


class Nagoomba(commands.Cog):

	def __init__(self, azami):
		self.azami = azami

	@commands.command(description='Stare')
	def stare(self, ctx):
		display.nagoombaimg('stare')



def setup(azami):
	azami.add_cog(Nagoomba(azami))