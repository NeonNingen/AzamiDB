import discord
from discord.ext import commands

class Mod(commands.Cog):

	def __init__(self, client):
		self.client = client

	@commands.command()
	async def ping(ctx):
		await ctx.send(f'Pong! :ping_pong: {round(azami.latency * 1000)}ms.')



def setup(client):
	client.add_cog(Mod(client))