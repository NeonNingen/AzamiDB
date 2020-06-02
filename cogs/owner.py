import discord
from discord.ext import commands
from discord.ext.commands import NotOwner, MissingRequiredArgument

class Owner(commands.Cog, command_attrs=dict(hidden=True)):

	def __init__(self, azami):
		self.azami = azami
		self.hidden = True

	@commands.command(name='load', description='Owner of Azami Only')
	@commands.is_owner()
	async def load(self, ctx, extension):
		extension = extension.lower()
		self.azami.load_extension(f'cogs.{extension}')
		print(f"The cog, {extension} has loaded")
		await ctx.send(f"The cog, {extension.capitalize()} has loaded")

	@commands.command(name='unload', description='Owner of Azami Only')
	@commands.is_owner()
	async def unload(self, ctx, extension):
		extension = extension.lower()
		self.azami.unload_extension(f'cogs.{extension}')
		print(f"The cog, {extension} has unloaded")
		await ctx.send(f"The cog, {extension.capitalize()} has unloaded")

	@commands.command(name='reload', description='Owner of Azami Only')
	@commands.is_owner()
	async def _reload(self, ctx, extension):
		extension = extension.lower()
		self.azami.unload_extension(f'cogs.{extension}')
		self.azami.load_extension(f'cogs.{extension}')
		print(f"The cog, {extension} has reloaded")
		await ctx.send(f"The cog, {extension.capitalize()} has reloaded")

	@commands.command(aliases=['hban'], description="You can ban anyone, even if they're not in the server")
	@commands.has_permissions(ban_members=True)
	async def hackban(self, ctx, user_id: int):
		author = ctx.message.author
		guild = author.guild

		user = guild.get_member(user_id)
		if user is not None:
			return await ctx.invoke(self.ban, user=user)

		try:
			await self.azami.http.ban(user_id, guild.id, 0)
			await ctx.send(f'User: <@{user_id}> has been banned')
			await ctx.message.delete()
		except discord.NotFound:
			await ctx.message.delete()
			await ctx.send(f'User: <@{user_id}> has cannot be found')
		except discord.errors.Forbidden:
			await ctx.message.delete()
			await ctx.send(f'User: <@{user_id}> has not been banned due to your permissions')

	@commands.command(description='Owner of Azami Only', aliases=['bi', 'boti'])
	@commands.is_owner()
	async def botinvite(self, ctx):
		await ctx.send("Here's the bot invite:\n" \
		"https://discord.com/oauth2/authorize?client_id=639574438794231818&permissions=8&scope=bot")

	@commands.command(description='Owner of Azami Only', 
					  aliases=['ownerhelp', 'oh', 'ownerh'])
	@commands.is_owner()
	async def owner(self, ctx):
		cog = self.azami.get_cog('Owner')
		commands = cog.get_commands()
		await ctx.send([c.name for c in commands])

	@load.error
	async def load_error(self, ctx, error):
		if isinstance(error, NotOwner):
			await ctx.send("You must be the owner of this bot to use this command")
		elif isinstance(error, commands.CommandInvokeError):
			await ctx.send(f"That cog doesn't exist")
		elif isinstance(error, MissingRequiredArgument):
			await ctx.send("Requires an argument")

	@unload.error
	async def unload_error(self, ctx, error):
		if isinstance(error, NotOwner):
			await ctx.send("You must be the owner of this bot to use this command")
		elif isinstance(error, commands.CommandInvokeError):
			await ctx.send("Invalid arguement, did you check if it's lower case or missing an arguement?")
		elif isinstance(error, MissingRequiredArgument):
			await ctx.send("Requires an argument")

	@_reload.error
	async def reload_error(self, ctx, error):
		if isinstance(error, NotOwner):
			await ctx.send("You must be the owner of this bot to use this command")
		elif isinstance(error, commands.CommandInvokeError):
			await ctx.send("Invalid arguement, did you check if it's lower case or missing an arguement?")
		elif isinstance(error, MissingRequiredArgument):
			await ctx.send("Requires an argument")

	@hackban.error
	async def hackban_error(self, ctx, error):
		if isinstance(error, NotOwner):
			await ctx.send("You must be the owner of this bot to use this command")
		elif isinstance(error, commands.MissingPermissions):
			await ctx.send("You cannot use this command")
		elif isinstance(error, MissingRequiredArgument):
			await ctx.send("Enter as follows: `ab!hackban {user_id}`")

	@botinvite.error
	async def botinvite_error(self, ctx, error):
		if isinstance(error, NotOwner):
			await ctx.send("You must be the owner of this bot to use this command")
		elif isinstance(error, commands.CommandInvokeError):
			await ctx.send("Invalid arguement, did you check if it's lower case or missing an arguement?")
		elif isinstance(error, MissingRequiredArgument):
			await ctx.send("Requires an argument")

	@owner.error
	async def owner_error(self, ctx, error):
		if isinstance(error, NotOwner):
			await ctx.send("You must be the owner of this bot to use this command")
		elif isinstance(error, commands.CommandInvokeError):
			await ctx.send("Invalid arguement, did you check if it's lower case or missing an arguement?")
		elif isinstance(error, MissingRequiredArgument):
			await ctx.send("Requires an argument")
		
def setup(azami):
	azami.add_cog(Owner(azami))