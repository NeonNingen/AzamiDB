import discord
from discord.ext import commands

class Basic(commands.Cog):

	def __init__(self, azami):
		self.azami = azami

	@commands.command()
	async def hello(ctx):
		await ctx.send(f"Hello!, {ctx.author.mention}")

	@commands.command()
	async def ping(ctx):
		await ctx.send(f'Pong! :ping_pong: {round(self.azami.latency * 1000)}ms.')

	@commands.command()
	async def invite(ctx):
		await ctx.send("The server invite: https://discord.gg/rRb23dt")

def setup(azami):
	azami.add_cog(Basic(azami))