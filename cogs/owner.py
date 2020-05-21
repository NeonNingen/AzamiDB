import discord
from discord.ext import commands
from discord.ext.commands import NotOwner, MissingRequiredArgument

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
		if isinstance(error, NotOwner):
			await ctx. send("You must be the owner of this bot to use this command")
			return
		elif isinstance(error, commands.CommandInvokeError):
			await ctx.send(f"That cog doesn't exist")
			return
		elif isinstance(error, MissingRequiredArgument):
			await ctx.send("Requires an argument")
			return
		return error

	@unload.error
	async def unload_error(self, ctx, error):
		if isinstance(error, NotOwner):
			await ctx. send("You must be the owner of this bot to use this command")
			return
		elif isinstance(error, commands.CommandInvokeError):
			await ctx.send("Invalid arguement, did you check if it's lower case or missing an arguement?")
			return
		elif isinstance(error, MissingRequiredArgument):
			await ctx.send("Requires an argument")
			return
		return error

	@_reload.error
	async def reload_error(self, ctx, error):
		if isinstance(error, NotOwner):
			await ctx. send("You must be the owner of this bot to use this command")
			return
		elif isinstance(error, commands.CommandInvokeError):
			await ctx.send("Invalid arguement, did you check if it's lower case or missing an arguement?")
			return
		elif isinstance(error, MissingRequiredArgument):
			await ctx.send("Requires an argument")
			return
		return error
		
def setup(azami):
	azami.add_cog(Owner(azami))