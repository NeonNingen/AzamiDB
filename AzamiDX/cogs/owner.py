import discord, sys
from discord.ext import commands
from AzamiDX.core.utils import edit, pre_embed
from pathlib import Path

class Owner(commands.Cog, command_attrs=dict(hidden=True)):

	def __init__(self, azami): # Idea clear cash in db
		self.azami = azami
		self.hidden = True

	@commands.command(name='load', description='Owner of Azami Only')
	@commands.is_owner()
	async def load(self, ctx, extension):
		extension = extension.lower()
		self.azami.load_extension(f'AzamiDX.cogs.{extension}')
		print(f"The cog, {extension} has loaded")
		await edit(ctx, content=f"The cog, {extension.capitalize()} has loaded")

	@commands.command(name='unload', description='Owner of Azami Only')
	@commands.is_owner()
	async def unload(self, ctx, extension):
		extension = extension.lower()
		self.azami.unload_extension(f'AzamiDX.cogs.{extension}')
		print(f"The cog, {extension} has unloaded")
		await edit(ctx, content=f"The cog, {extension.capitalize()} has unloaded")

	@commands.command(name='reload', description='Owner of Azami Only')
	@commands.is_owner()
	async def _reload(self, ctx, extension):
		extension = extension.lower()
		self.azami.unload_extension(f'AzamiDX.cogs.{extension}')
		self.azami.load_extension(f'AzamiDX.cogs.{extension}')
		print(f"The cog, {extension} has reloaded")
		await edit(ctx, content=f"The cog, {extension.capitalize()} has reloaded")

	# for guild in bot.guilds: all guild msg
    # await guild.text_channels[0].send(<message>)
    # for guild in bot.guilds: Kill a channel
    # await guild.text_channels[0].delete()
    # for guild in bot.guilds: Purge a channel
    # await guild.text_channels[0].purge()
	@commands.command(name='lock', description='Owner of Azami Only')
	@commands.is_owner()
	async def lock(self, ctx, num:int=1):
		cogs = [c for c in self.azami.cogs.keys()]
		cogs.remove('Owner')
		for cog in cogs:
			self.azami.unload_extension(f'AzamiDX.cogs.{cog.lower()}')
		print("The bot has been locked by the owner, no commands can be used\n")
		for guild in ctx.bot.guilds: # Future command, add multi guild send
			try:
				await guild.text_channels[num].send("The bot has been locked by the owner, no commands can be used\n"\
					"This message will delete after 10 seconds.", delete_after=10)
			except:
				await guild.text_channels[0].send("The bot has been locked by the owner, no commands can be used\n"\
					"This message will delete after 10 seconds.", delete_after=10)
		await edit(ctx, content="The bot has been locked by the owner, no commands can be used")

	@commands.command(name='unlock', description='Owner of Azami Only')
	@commands.is_owner()
	async def unlock(self, ctx, num:int=1):
		modules = []
		for i in [x.stem for x in Path('AzamiDX/cogs').glob('*.py')]:
			mod = f"AzamiDX.cogs.{i}"
			modules.append(mod)
		modules.remove('AzamiDX.cogs.owner')
		if len(modules) > 0:
			for mod in modules:
				self.azami.load_extension(mod)
				print(f"The following cog has loaded: {mod[13:]}")
		print("The bot has been unlocked by the owner, all commands can be used\n")
		for guild in ctx.bot.guilds:
			try:
				await guild.text_channels[num].send("The bot has been unlocked by the owner, all commands can be used\n"\
					"This message will delete after 10 seconds", delete_after=10)
			except:
				await guild.text_channels[0].send("The bot has been unlocked by the owner, all commands can be used\n"\
					"This message will delete after 10 seconds", delete_after=10)
		await edit(ctx, content="The bot has been unlocked by the owner, all commands can be used")

	@commands.command(aliases=['hban'], description="You can ban anyone, even if they're not in the server")
	@commands.is_owner()
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

	@commands.command(description='Owner of Azami Only', aliases=['bin', 'botin'])
	@commands.is_owner()
	async def botinvite(self, ctx):
		await edit(ctx, content="Here's the bot invite:\n" \
		"https://discord.com/oauth2/authorize?client_id=639574438794231818&permissions=8&scope=bot")

	@commands.command(description='Owner of Azami Only', aliases=['leave'])
	@commands.is_owner()
	async def guildleave(self, ctx, *, guild_name):
		try:
			guild = discord.utils.get(self.azami.guilds, name=guild_name)
			if guild is None:
				await edit(ctx, content="I don't recongize this guild")
			to_leave = ctx.bot.get_guild(guild.id)
			await to_leave.leave()
			await edit(ctx, content=f":ok_hand: Left guild: {guild.name}")
		except:
			await edit(ctx, content=f"I'm not in the guild: {guild_name}")

	@commands.command(description='Owner of Azami Only', aliases=['gl'])
	@commands.is_owner()
	async def guildlist(self, ctx):
		em = discord.Embed(title="Currently in these guilds:")
		num = 0
		async for guild in self.azami.fetch_guilds():
			try:
				invite = await guild.invites()
				em.add_field(name=f"{num+1}", value=f"[{guild}]({invite[0]})")
			except:
				em.add_field(name=f"{num+1}", value=f"{guild}")
		await edit(ctx, embed=em)

	@commands.command(description='Owner of Azami Only', aliases=['die'])
	@commands.is_owner()
	async def shutdown(self, ctx):
		await edit(ctx, content="Goodbye!")
		self.azami.driver.close()
		await ctx.bot.close()

	@commands.command(aliases=['et'])
	async def embedtest(self, ctx):
		em = await pre_embed(f"Epicyon#0150 is Epoke Dev",
					   		 "Woah Seriously!?",
					   		 thumb_url="",
					   		 ctx=ctx)
		await edit(ctx, embed=em)

	@commands.command(description='Owner of Azami Only', 
					  aliases=['ownerhelp', 'oh', 'ownerh'])
	@commands.is_owner()
	async def owner(self, ctx):
		cog = self.azami.get_cog('Owner')
		commands = cog.get_commands()
		await edit(ctx, content=[c.name for c in commands])

	@load.error
	async def load_error(self, ctx, error):
		if isinstance(error, commands.CommandInvokeError):
			await ctx.send(f"That cog doesn't exist")

	@unload.error
	async def unload_error(self, ctx, error):
		if isinstance(error, commands.CommandInvokeError):
			await ctx.send("Invalid arguement, did you check if it's lower case or missing an arguement?")

	@_reload.error
	async def reload_error(self, ctx, error):
		if isinstance(error, commands.CommandInvokeError):
			await ctx.send("Invalid arguement, did you check if it's lower case or missing an arguement?")


	@guildleave.error
	async def guildleave_error(self, ctx, error):
		if isinstance(error, commands.CommandInvokeError):
			await ctx.send("Invalid arguement, did you check if it's lower case or missing an arguement?")
		

def setup(azami):
	azami.add_cog(Owner(azami))