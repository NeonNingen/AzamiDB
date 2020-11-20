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
	async def day(self, ctx):
		await ctx.send(display.nagoombaimg('day'))

	@commands.command()
	async def basedbot(self, ctx):
		await ctx.send(display.nagoombaimg('basedbot'))


	@commands.command()
	async def cbt(self, ctx):
		em = await pre_embed(titl="Just got CBT'd. Didn't like it.",
							 image_url=display.nagoombaimg('cbt'))

		await ctx.send(embed=em)

	@commands.command()
	async def pruebala(self, ctx):
		em = await pre_embed(titl="es cocaina")

		await ctx.send(embed=em)
		await ctx.send(display.nagoombaimg('pruebala'))

	@commands.command()
	async def basado(self, ctx):
		em = await pre_embed(titl="Basado en que?",
							 image_url=display.nagoombaimg('basado'))

		await ctx.send(embed=em)
		await ctx.send("https://www.youtube.com/watch?v=q-Rqdgna3Yw")

	@commands.command()
	async def cocke(self, ctx):
		em = await pre_embed(titl="Haruka c-")
		await ctx.send(embed=em)
		await ctx.send("https://www.youtube.com/watch?v=QuzxNw4r0uc")

def setup(azami):
	azami.add_cog(Nagoomba(azami))