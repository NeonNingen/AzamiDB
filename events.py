import discord, os, random, json
from discord.ext import commands, tasks
from discord.ext.commands import CommandNotFound
from itertools import cycle

def get_prefix(azami, message):
	with open('prefix.json', 'r') as fp:
		prefixes = json.load(fp)

	return prefixes[str(message.guild.id)]

azami = commands.Bot(command_prefix = get_prefix,
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

	@tasks.loop(seconds=3600)
	async def change_status():
		await azami.change_presence(activity=discord.Game(next(status)))

	@azami.event
	async def on_member_join(member):
		print(f"{member} has joined the server")

	@azami.event
	async def on_member_remove(member):
		print(f"{member} has left/kick from the server")

	@azami.event
	async def on_guild_join(guild):
		with open('prefix.json', 'r') as fp:
			prefixes = json.load(fp)

		prefixes[str(message.guild.id)] = 'a!'

		with open('prefix.json', 'w') as fp:
			json.dump(prefixes, fp, indent=4)

	@azami.event
	async def on_guild_remove(guild):
		with open('prefix.json', 'r') as fp:
			prefixes = json.load(fp)

		prefixes.pop(str(guild.id))

		with open('prefix.json', 'w') as fp:
			json.dump(prefixes, fp, indent=4)


	@azami.event
	async def on_command_error(ctx, error):
		if isinstance(error, CommandNotFound):
			await ctx.send("Invalid command, did you type that right?")
			return
		raise error

def main():
	event_azami()
	azami.run(os.environ['DISCORD_TOKEN'])
	#token = open("token.txt", "r")
	#azami.run(token.read())

