import discord
from discord.ext import commands

class Maths(commands.Cog):

	def __init__(self, azami):
		self.azami = azami

	@commands.command()
	async def add(self, ctx, a: float, b: float):
		await ctx.send(f"{a} + {b} = {a + b}")

	@commands.command(aliases = ['takeaway'])
	async def subtract(self, ctx, a: float, b: float):
		await ctx.send(f"{a} - {b} = {a - b}")

	@commands.command(aliases = ['times'])
	async def multiply(self, ctx, a: float, b: float):
		await ctx.send(a * b)

	@commands.command(aliases = ['division'])
	async def divide(self, ctx, a: float, b: float):
		await ctx.send(a / b)
	



def setup(azami):
	azami.add_cog(Maths(azami))