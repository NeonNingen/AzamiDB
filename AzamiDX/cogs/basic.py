import discord
from discord.ext import commands
from AzamiDX.core.utils import edit

class Basic(commands.Cog):

	def __init__(self, azami):
		self.azami = azami

	@commands.command(description='Hi!')
	async def hello(self, ctx):
		await edit(ctx, content=f"Hello!, {ctx.author.mention}")

	@commands.command(description='Get the latency of the bot')
	async def ping(self, ctx):
		await edit(ctx, content=f'Pong! :ping_pong: {round(self.azami.latency * 1000)}ms.')

	@commands.command(description='Gets the Wholesome Society invite link')
	async def invite(self, ctx):
		await edit(ctx, content="The server invite: https://discord.gg/rRb23dt")

def setup(azami):
	azami.add_cog(Basic(azami))