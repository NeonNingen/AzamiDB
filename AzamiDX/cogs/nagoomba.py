import discord
from discord.ext import commands
from AzamiDX.etc.img import display
from AzamiDX.core.utils import pre_embed

class Nagoomba(commands.Cog):

	def __init__(self, azami):
		self.azami = azami

	@commands.command()
	async def stare(self, ctx):
		await ctx.send(display.nagoombaimg('stare'))

	@commands.command()
	async def ichireal(self, ctx):
		await ctx.send(display.nagoombaimg('ichireal'))

	@commands.command()
	async def ichifake(self, ctx):
		await ctx.send(display.nagoombaimg('ichifake'))

	@commands.command()
	async def cbt(self, ctx):
		em = await pre_embed(titl="Just got CBT'd. Didn't like it.",
							 image_url=display.nagoombaimg('cbt'))

		await ctx.send(embed=em)

def setup(azami):
	azami.add_cog(Nagoomba(azami))