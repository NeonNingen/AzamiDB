import discord, os, random, time
from discord.ext import commands, tasks
from discord.ext.commands import CommandNotFound, CheckFailure, NoPrivateMessage, MissingRequiredArgument
from asyncio import sleep
from pathlib import Path
from AzamiDX.core.utils import edit, error_on_message, pre_embed

class AzamiBot(commands.AutoShardedBot):
	# Subclassing Bot allows for more unique event handling

	def __init__(self):
		self.command_prefix = "ab!"
		self.description = "Azami, An all purpose bot!"
		self.owner_id = 288022950576390144
		super().__init__(self.command_prefix)


		self.modules = []

		for i in [x.stem for x in Path('AzamiDX/cogs').glob('*.py')]:
			mod = f"AzamiDX.cogs.{i}"
			self.modules.append(mod)

		self.start_time = time.time()
		

	@staticmethod
	async def delete_message(message: discord.Message):
		if not isinstance(message.channel, discord.DMChannel):
			try:
				return await message.delete()
			except discord.Forbidden:
				error_on_message(message, "No permissions to delete message")

	
	def load_modules(self, modules_list: list):
		if len(modules_list) > 0:
			for mod in modules_list:
				try:
					self.load_extension(mod)
					print(f"The following cog has loaded: {mod[13:]}")
				except Exception as e:
					print(f"Could not load cog '{mod}'' -> '{e}'")

	async def on_ready(self):
		print(f"{self.user.name} has started!\n" \
			f'Started at: {time.strftime("%I:%M %p")}\n')

		if self.shard_count > 1:
			for x in range(0, self.shard_count):
				await self.change_presence(activity=discord.Activity(
					name=(
						 f'Use {self.command_prefix}help for help| Shard' \
						 f'{x + 1}/{self.shard_count}'),
					type=discord.ActivityType.playing), shard_id=x)
				await sleep(5)
		else:
			await self.change_presence(activity=discord.Activity(
				name=(
					f"{self.command_prefix}help | {len(self.guilds)} guilds | V2.0"),
				type=discord.ActivityType.listening))

		print("Currently in these guilds:")
		async for guild in self.fetch_guilds():
			print(f"{guild.name}")

		print()
		self.load_modules(self.modules)
		finished_time = time.time() - self.start_time

		print(f"Finished loading! Azami took: {round(finished_time, 3)} seconds\n")


	async def on_member_join(self, member):
		print(f"{member} has joined the guild")


	async def on_member_leave(self, member):
		print(f"{member} has left/kick from the guild")

	'''
	async def on_command_error(self, ctx, error):
		if isinstance(error, NoPrivateMessage):
			await edit(ctx, content='\N{HEAVY EXCLAMATION MARK SYMBOL} Only usable on Servers', ttl=5)
		elif isinstance(error, CheckFailure):
			await edit(ctx, content='\N{HEAVY EXCLAMATION MARK SYMBOL} No Permissions to use this command', ttl=5)
		elif isinstance(error, MissingRequiredArgument):
			await edit(ctx, content='\N{HEAVY EXCLAMATION MARK SYMBOL} Missing Argument', ttl=5)
		elif isinstance(error, CommandNotFound):
			await edit(ctx, content='Invalid command, did you type that right?', ttl=10)
	'''
	async def on_message(self, message):
		if not message.author.bot:
			if message.guild == None:
				await message.channel.send("Commands only work in a guild I reside in", delete_after=5)
			else:
				await self.process_commands(message)


	async def on_guild_join(self, guild: discord.Guild):
		print(f"{self.user.name} has joined {guild.name}")
		cogs = [c for c in self.cogs.keys()]
		cogs.remove('Owner')
		store = 0
		for cog in cogs:
			cogc = self.get_cog(cog).get_commands()
			store += len(cogc)
		for channel in guild.text_channels: # cogc = cog commands
			if channel.permissions_for(guild.me).send_messages:
				embed = discord.Embed(title="Hi there!",
									  description=f"{guild.name}, I'm so excited to be here!",
									  color=discord.Color.gold())
				embed.set_thumbnail(url=guild.icon_url)
				embed.set_footer(text=f"I'm in {len(self.guilds)} guilds!")
				value1 = f"I'm an all purpose bot with currently:\n **{len(cogs)} cogs** and **{store} commands**"
				value2 = f"It's a pleasure to make your Acquaintance, {guild.owner.mention}"
				embed.add_field(name=f"Hi, my name is {self.user.name}", value=value1)
				embed.add_field(name=f"To read about my commands, do {self.command_prefix}help", value=value2)
				await channel.send(embed=embed)
			break

	async def on_guild_leave(self, guild: discord.Guild):
		print(f"{self.user.name} has left {guild.name}")


