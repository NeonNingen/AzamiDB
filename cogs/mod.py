import discord
from discord.ext import commands

class Mod(commands.Cog):

	def __init__(self, azami, ctx):
		self.azami = azami
		self.ctx = ctx

	@commands.command()
	async def ping(self):
		await self.ctx.send(f'Pong! :ping_pong: {round(self.azami.latency * 1000)}ms.')



def setup(azami):
	azami.add_cog(Mod(azami))