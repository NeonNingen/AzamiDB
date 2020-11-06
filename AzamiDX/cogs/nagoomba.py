import discord
from discord.ext import commands
from AzamiDX.etc.img import display
from AzamiDX.core.utils import pre_embed

class Nagoomba(commands.Cog):

	def __init__(self, azami):
		self.azami = azami

	async def stare(self, ctx):
		await ctx.send(display.nagoombaimg('stare'))

	async def ichireal(self, ctx):
		await ctx.send(display.nagoombaimg('ichireal'))

	async def ichifake(self, ctx):
		await ctx.send(display.nagoombaimg('ichifake'))

	async def cbt(self, ctx):
		await pre_embed(titl="Just got CBT'd. Didn't like it.",
						image_url=display.nagoombaimg('cbt'))

def setup(azami):
	azami.add_cog(Nagoomba(azami))