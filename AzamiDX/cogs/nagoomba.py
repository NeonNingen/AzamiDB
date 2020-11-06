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
		url = display.nagoombaimg('ichireal')
		await ctx.send(url)

	async def cbt(self, ctx):
		url = display.nagoombaimg('cbt')
		await pre_embed(titl="Just got CBT'd. Didn't like it.",
						image_url=display.nagoombaimg('cbt'))

def setup(azami):
	azami.add_cog(Nagoomba(azami))