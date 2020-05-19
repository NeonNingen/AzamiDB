import discord
from discord.ext import commands

class Maths(commands.Cog):

	def __init__(self, azami):
		self.azami = azami

	@commands.command()
	async def add(ctx, a: float, b: float):
		await ctx.send(f"{a} + {b} = {a + b}")

	@commands.command(aliases = ['takeaway'])
	async def subtract(ctx, a: float, b: float):
		await ctx.send(f"{a} - {b} = {a - b}")

	@commands.command(aliases = ['times'])
	async def multiply(ctx, a: float, b: float):
		await ctx.send(a * b)

	@commands.command(aliases = ['division'])
	async def divide(ctx, a: float, b: float):
		await ctx.send(a / b)
	



def setup(azami):
	azami.add_cog(Maths(azami))