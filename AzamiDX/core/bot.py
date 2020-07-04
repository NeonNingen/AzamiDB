import datetime, discord, os, psycopg2, random, time 
from discord.ext import commands, tasks
from asyncio import sleep
from pathlib import Path
from selenium import webdriver
from AzamiDX.core.webdriver import get_driver
from AzamiDX.core.utils import error_on_message, pre_embed, color_list, get_prefix
from AzamiDX.etc.etccont.verify import verify

try:
	db = psycopg2.connect(
	host="ec2-54-75-248-49.eu-west-1.compute.amazonaws.com",
	database="defh9ng1qcsr3r",
	user="yaffdhqkqalpvx",
	password="4bd878bee114c6476d9775135dfb8a28f324a3ac17f4996053df95072d7fcc38")
	mycursor = db.cursor()
	print("The database has loaded")
except:
	db = ""
	mycursor = ""
	print("None database mode activated")


class AzamiBot(commands.AutoShardedBot):
	# Subclassing Bot allows for more unique event handling

	def __init__(self): 
		self.db = db
		self.mycursor = mycursor
		try:
			self.driver = get_driver()
		except:
			self.driver = webdriver.Chrome('./chromedriver')
		self.driver.minimize_window()
		
		self.command_prefix = get_prefix
		self.description = "Azami, An all purpose bot!"
		self.owner_id = 288022950576390144
		super().__init__(self.command_prefix)

		self.modules = []
		self.id_store = []

		for i in [x.stem for x in Path('AzamiDX/cogs').glob('*.py')]:
			mod = f"AzamiDX.cogs.{i}"
			self.modules.append(mod)

		self.start_time = time.time()

		
	async def restrictor(self, ctx):
		id_list = set(self.id_store)
		if ctx.message.author.id in id_list:
			await ctx.send("This command is already active or another command is in use")
			return True
		else:
			self.id_store.append(ctx.message.author.id)
			return False


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

	async def original_prefix(self, azami, message):
			prefix = await get_prefix(azami, message)
			prefix = prefix[2]
			return prefix

	async def on_ready(self):
		start_time = datetime.datetime.now().strftime(f"%a %d %B %Y %H:%M:%S")

		print(f"{self.user.name} has started!\n" \
			f'Started at: {time.strftime("%I:%M %p")}\n')

		self.og_command_prefix = await self.original_prefix(self, discord.Message)

		if self.shard_count > 1:
			for x in range(0, self.shard_count):
				await self.change_presence(activity=discord.Activity(
					name=(
						 f'Use {self.og_command_prefix}help for help| Shard' \
						 f'{x + 1}/{self.shard_count}'),
					type=discord.ActivityType.playing), shard_id=x)
				await sleep(5)
		else:
			await self.change_presence(activity=discord.Activity(
				name=(
					f"{self.og_command_prefix}help | {len(self.guilds)} guilds | V2.1"),
				type=discord.ActivityType.listening))

		num = 0

		print("Currently in these guilds:")
		async for guild in self.fetch_guilds():
			num += 1
			print(f"{guild.name}")

		print()
		self.load_modules(self.modules)
		finished_time = time.time() - self.start_time

		print(f"Finished loading! Azami took: {round(finished_time, 3)} seconds\n")

		em = discord.Embed(title="Azami has started!", color=discord.Color.blurple())
		em.add_field(name="Currently in: ", value=f"{num} guilds")
		em.add_field(name="Version: ", value="V2.1")
		em.add_field(name="Start Date and Time: ", value=f'{start_time}')
		em.add_field(name="Load Time", value=f"{round(finished_time, 2)} seconds")
		em.set_thumbnail(url=self.user.avatar_url)

		channel = self.get_channel(728956265337978921)
		await channel.send(embed=em)


	
	async def on_member_join(self, member):
		if member.guild.id == 110373943822540800:
			pass
		else:
			print(f"{member} has joined {member.guild}")

		if member.bot:
			pass
		else:
			if member.guild.id == 699997006277509260:
				channel = self.get_channel(718406709814624288)
				em = discord.Embed()
				em.title = f"Welcome! {member.name}"
				em.description = verify(self, channel, member)
				em.color = color_list()
				em.set_thumbnail(url=member.avatar_url)
				em.set_image(url='https://media0.giphy.com/media/83KcvGkJuNfoY/source.gif')
				message = await channel.send(embed=em)

				role = discord.utils.get(member.guild.roles, name="Toads")
				emoji = u"\u2705"
				await message.add_reaction(emoji)
				while True:
					reaction, user = await self.wait_for('reaction_add', check=lambda r, u: member)
					if user == member:
						await user.add_roles(role)
						await message.remove_reaction(emoji, user)
						await message.clear_reaction(emoji)
						await channel.send(f"You have successful verified: {member.name}!")
						return
					elif str(user) == f"{self.user.name}#{self.user.discriminator}":
						pass
					elif user.bot:
						pass
					elif role in user.roles:
						pass
					else:
						await message.remove_reaction(emoji, user)
						await channel.send(f"{member.name} has to react not you: {user.name}!", delete_after=3)

	async def on_member_leave(self, member):
		print(f"{member} has left/kick from {member.guild}")
		
	
	async def on_message(self, message):
		if not message.author.bot:
			if message.guild == None:
				await message.channel.send("Commands only work in a guild I reside in", delete_after=5)
			else:
				await self.process_commands(message)


	async def on_guild_join(self, guild: discord.Guild):

		channel = self.get_channel(728911918483505163)
		date = datetime.datetime.now().strftime(f"%a %d %B %Y %H:%M:%S")
		join_em = discord.Embed(title=f"{guild.name}",
								description=f"Date Joined: {date}",
								color=discord.Color.green())
		join_em.add_field(name="Owner", value=guild.owner)
		join_em.add_field(name="Members", value=guild.member_count)
		join_em.add_field(name="Region", value=guild.region)
		join_em.set_thumbnail(url=guild.icon_url)
		try:
			invite = await guild.invites()
			invite = invite[0]
			join_em.add_field(name="Invite", value=f"[Invite Link]({invite})")
		except:
			pass

		await channel.send(embed=join_em)

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
				embed.add_field(name=f"To read about my commands, do {self.og_command_prefix}help", value=value2)
				embed.add_field(name=f"My owner is: ", value='<@288022950576390144>')
				try:
					embed.add_field(name=f"My support server is: ", value='[Gusty Garden](https://discord.gg/rRb23dt)')
				except:
					pass
				await channel.send(embed=embed)
			break

	async def on_guild_remove(self, guild: discord.Guild):
		channel = self.get_channel(728911934291837020)
		date = datetime.datetime.now().strftime(f"%a %d %B %Y %H:%M:%S")
		leave_em = discord.Embed(title=f"{guild.name}",
								description=f"Date Left: {date}",
								color=discord.Color.orange())

		leave_em.set_thumbnail(url=guild.icon_url)

		await channel.send(embed=leave_em)

		print(f"{self.user.name} has left {guild.name}")

	
