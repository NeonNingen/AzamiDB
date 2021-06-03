import discord, json
from discord.ext import commands
from AzamiDX.core.utils import edit

class rank(commands.Cog):

	def __init__(self, azami):
		self.azami = azami

	@commands.command(description='Yo')
	async def hellotest(self, ctx):
		await edit(ctx, content=f"Hello!, {ctx.author.mention}")

def setup(azami):
	azami.add_cog(rank(azami))