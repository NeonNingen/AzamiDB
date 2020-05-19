import discord
from discord.ext import commands
from random import randint

class Dnd(commands.Cog):

	def __init__(self, azami):
		self.azami = azami

	@commands.command()
	async def d4(self, ctx):
		await ctx.send(f"You rolled: {randint(1, 4)}")

	@commands.command()
	async def d6(self, ctx):
		await ctx.send(f"You rolled: {randint(1, 6)}")

	@commands.command()
	async def d8(self, ctx):
		await ctx.send(f"You rolled: {randint(1, 8)}")

	@commands.command()
	async def d10(self, ctx):
		await ctx.send(f"You rolled: {randint(1, 10)}")

	@commands.command()
	async def d100(self, ctx):
		await ctx.send(f"You rolled: {randint(1, 100)}")

	@commands.command()
	async def d12(self, ctx):
		await ctx.send(f"You rolled: {randint(1, 12)}")

	@commands.command()
	async def d20(self, ctx):
		await ctx.send(f"You rolled: {randint(1, 20)}")


def setup(azami):
	azami.add_cog(Dnd(azami))