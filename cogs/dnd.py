import discord
from discord.ext import commands
from random import randint

class Dnd(commands.Cog):

	def __init__(self, azami):
		self.azami = azami

	@commands.command(description='To roll do `a!roll NdN`')
	async def roll(self, ctx, dice: str):
		try:
			rolls, limit = map(int, dice.split('d'))
		except Exception:
			await ctx.send('The format has to be in NdN!')
			return

		result = ', '.join(str(randint(1, limit)) for r in range(rolls))
		await ctx.send(result)


def setup(azami):
	azami.add_cog(Dnd(azami))