import discord
from discord.ext import commands
from AzamiDX.etc.img import display
from AzamiDX.core.utils import pre_embed

class Nagoomba(commands.Cog):

	def __init__(self, azami):
		self.azami = azami

	@commands.command(description='Stare')
	async def stare(self, ctx):
		url = display.nagoombaimg('stare')
		await pre_embed(image_url=url)

def setup(azami):
	azami.add_cog(Nagoomba(azami))