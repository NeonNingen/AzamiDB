import discord
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument

class Maths(commands.Cog):

	def __init__(self, azami):
		self.azami = azami

	@commands.command(aliases = ['addition', 'plus', '+'])
	async def add(self, ctx, a: float, b: float):
		await ctx.send(f"{a} + {b} = {a + b}")

	@commands.command(aliases = ['takeaway', 'minus', '-'])
	async def subtract(self, ctx, a: float, b: float):
		await ctx.send(f"{a} - {b} = {a - b}")

	@commands.command(aliases = ['times', '*'])
	async def multiply(self, ctx, a: float, b: float):
		await ctx.send(a * b)

	@commands.command(aliases = ['division', '/'])
	async def divide(self, ctx, a: float, b: float):
		await ctx.send(a / b)

	@add.error
	async def add_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument):
			await ctx.send("Requires an argument")
		elif isinstance(error, commands.BadArgument):
			await ctx.send("Invalid arguement, this command only takes floats")
			

	@subtract.error
	async def subtract_error_1(self, ctx, error):
		if isinstance(error, MissingRequiredArgument):
			await ctx.send("Requires an argument")

	@subtract.error
	async def subtract_error_2(self, ctx, error):
		if isinstance(error, commands.BadArgument):
			await ctx.send("Invalid arguement, this command only takes floats")

	@multiply.error
	async def multiply_error_1(self, ctx, error):
		if isinstance(error, MissingRequiredArgument):
			await ctx.send("Requires an argument")

	@multiply.error
	async def multiply_error_2(self, ctx, error):
		if isinstance(error, commands.BadArgument):
			await ctx.send("Invalid arguement, this command only takes floats")

	@divide.error
	async def divide_error_1(self, ctx, error):
		if isinstance(error, MissingRequiredArgument):
			await ctx.send("Requires an argument")

	@divide.error
	async def divide_error_2(self, ctx, error):
		if isinstance(error, commands.BadArgument):
			await ctx.send("Invalid arguement, this command only takes floats")
	



def setup(azami):
	azami.add_cog(Maths(azami))