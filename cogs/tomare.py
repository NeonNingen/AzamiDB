import discord
from discord.ext import commands

class Jojo(commands.Cog):

	def __init__(self, azami):
		self.azami = azami

	@commands.has_permissions(manage_messages = True)
	@commands.guild_only()
	@commands.command()
	async def tomare(self, ctx, time: int = 0):
		if time < 0 or time > 12:
			await ctx.send("Invalid time value. Time must be between 0 and 12 (inclusive)")
			return
		await ctx.channel.edit(slowmode_delay=time)
		if time > 0:
			await ctx.send(f"**{ctx.channel.mention} has been stopped in time. Time have frozen for {time} seconds**")
		else:
			await ctx.send(f"**Time resume for {ctx.channel.mention}**")

def setup(azami):
	azami.add_cog(Jojo(azami))