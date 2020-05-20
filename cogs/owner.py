import discord
from discord.ext import commands

class Owner(commands.Cog):

	def __init__(self, azami):
		self.azami = azami

	@commands.command(name='load', hidden=True)
	@commands.is_owner()
	async def load(self, ctx, extension):
		self.azami.load_extension(f'cogs.{extension}')
		print(f"The cog, {extension} has loaded")
		await ctx.send(f"The cog, {extension} has loaded")

	@commands.command(name='unload', hidden=True)
	@commands.is_owner()
	async def unload(self, ctx, extension):
		self.azami.unload_extension(f'cogs.{extension}')
		print(f"The cog, {extension} has unloaded")
		await ctx.send(f"The cog, {extension} has unloaded")

	@commands.command(aliases=['reload'], name='_reload', hidden=True)
	@commands.is_owner()
	async def _reload(self, ctx, extension):
		self.azami.unload_extension(f'cogs.{extension}')
		self.azami.load_extension(f'cogs.{extension}')
		print(f"The cog, {extension} has reloaded")
		await ctx.send(f"The cog, {extension} has reloaded")

	@load.error
	async def load_error(self, ctx, error):
		if isinstance(error, commands.CommandError):
			await ctx.send("Invalid arguement, did you check if it's lower case?")
		elif isinstance(error, commands.NotOwner):
			await ctx. send("You must be the owner of this bot to use this command")

	@unload.error
	async def unload_error(self, ctx, error):
		if isinstance(error, commands.CommandError):
			await ctx.send("Invalid arguement, did you check if it's lower case?")

	@_reload.error
	async def reload_error(self, ctx, error):
		if isinstance(error, commands.CommandError):
			await ctx.send("Invalid arguement, did you check if it's lower case?")


def setup(azami):
	azami.add_cog(Owner(azami))