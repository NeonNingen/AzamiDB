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

def setup(azami):
	azami.add_cog(Nagoomba(azami))