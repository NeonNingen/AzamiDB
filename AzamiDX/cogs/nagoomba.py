import discord
from discord.ext import commands
from AzamiDX.etc.img import display
from AzamiDX.core.utils import edit

class Nagoomba(commands.Cog):

	def __init__(self, azami):
		self.azami = azami

	@commands.command(description='Stare')
	def stare(self, ctx):
		em = discord.Embed()
		em.set_image(url=display.nagoombaimg('Stare'))
		await edit(ctx, embed=em)

def setup(azami):
	azami.add_cog(Nagoomba(azami))