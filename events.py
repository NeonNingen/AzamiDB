import discord, os, random
from discord.ext import commands, tasks
from discord.ext.commands import CommandNotFound, NoPrivateMessage
from itertools import cycle
from asyncio import sleep

azami = commands.Bot(command_prefix = 'a!',
					 description = "Azami, an all purpose bot!",
					 owner_id = 288022950576390144)

with open('status_quotes.txt', 'r') as f:
	status_quotes = f.read().splitlines()

random.shuffle(status_quotes)
status = cycle(status_quotes)	

def event_azami():

	for filename in os.listdir('./cogs'):
		if filename.endswith('.py'):
			azami.load_extension(f'cogs.{filename[:-3]}')
			print(f"The following cog has loaded: {filename[:-3]}")

	@azami.event
	async def on_ready():
		change_status.start()
		print(f"We have logged in as {azami.user}")	

	@tasks.loop(seconds=3000)
	async def change_status():
		await azami.change_presence(activity=discord.Activity(
			name=(
			f"{len(azami.guilds)} servers"), type=discord.ActivityType.watching))
		await sleep(300)
		await azami.change_presence(activity=discord.Game(next(status)))

	@azami.event
	async def on_member_join(member):
		print(f"{member} has joined the server")

	@azami.event
	async def on_member_remove(member):
		print(f"{member} has left/kick from the server")	

	
	@azami.event
	async def on_command_error(ctx, error):
		if isinstance(error, CommandNotFound):
			await ctx.send("Invalid command, did you type that right?")
			return
		elif isinstance(error, NoPrivateMessage):
			return
		return error

	@azami.event
	async def on_guild_join(guild: discord.Guild):
		cogs = [c for c in azami.cogs.keys()]
		store = 0
		for cog in cogs:
			cogc = azami.get_cog(cog).get_commands()
			store += len(cogc)
		for channel in guild.text_channels: # cogc = cog commands
			if channel.permissions_for(guild.me).send_messages:
				embed = discord.Embed(title="Hi there!",
									  description=f"{guild.name}, I'm so excited to be here!",
									  color=discord.Color.gold())
				embed.set_thumbnail(url=guild.icon_url)
				embed.set_footer(text=f"I'm in {len(azami.guilds)} guilds!")
				value1 = f"I'm an all purpose bot with currently:\n **{len(cogs)} cogs** and **{store} commands**"
				value2 = f"It's a pleasure to make your Acquaintance, {guild.owner.mention}"
				embed.add_field(name=f"Hi, my name is {azami.user.name}", value=value1)
				embed.add_field(name=f"To read about my commands, do {azami.command_prefix}help", value=value2)
				await channel.send(embed=embed)
			break
	
	@azami.check
	async def globally_block_dms(ctx):
		await ctx.send("Sorry I cannot do commands in DMs")
		

def main():
	event_azami()
	azami.run(os.environ['DISCORD_TOKEN'])
	#token = open("token.txt", "r")
	#azami.run(token.read())

