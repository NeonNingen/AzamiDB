import discord, os, random
from discord.ext import commands, tasks
from itertools import cycle

azami = commands.Bot(command_prefix = 'a!')
status_quotes = ["a!help",
				"Let's try to get along!",
				"I feel sleepy...",
				"I'm very unique",
				"I can compute at the speed of sound",
				"I'm made out of pure code",
				"Nya nya!",
				"https://discord.gg/rRb23dt",
				"I think therefore I am",
				"https://discord.com/oauth2/authorize?client_id=639574438794231818&permissions=8&scope=bot",
				"I was made to learn",
				"https://github.com/NeonNingen",
				"Beep Boop"]
random.shuffle(status_quotes)
status = cycle(status_quotes)

def commands_azami():
	
	@azami.command()
	async def hello(ctx):
		await ctx.send(f"Hello!, {ctx.author.mention}")

	@azami.command()
	async def ping(self, ctx):
		await ctx.send(f'Pong! :ping_pong: {round(azami.latency * 1000)}ms.')

	@azami.command()
	async def clear(ctx, amount = 5):
		await ctx.channel.purge(limit = amount + 1)

	@azami.command()
	async def load(ctx, extension):
		azami.load_extension(f'cogs.{extension}')
		print(f"The cog, {extension} has loaded")

	@azami.command()
	async def unload(ctx, extension):
		azami.unload_extension(f'cogs.{extension}')
		print(f"The cog, {extension} has unloaded")

	@azami.command()
	async def reload(ctx, extension):
		azami.unload_extension(f'cogs.{extension}')
		azami.load_extension(f'cogs.{extension}')
		print(f"The cog, {extension} has reloaded")

def event_azami():

	for filename in os.listdir('./cogs'):
		if filename.endswith('.py'):
			azami.load_extension(f'cogs.{filename[:-3]}')
			print(f"The following cog has loaded: {filename[:-3]}")

	@azami.event
	async def on_ready():
		change_status.start()
		print("We have logged in as {0.user}".format(azami))

	@tasks.loop(seconds=3600)
	async def change_status():
		await azami.change_presence(activity=discord.Game(next(status)))

	@azami.event
	async def on_member_join(member):
		print(f"{member} has joined the server")

	@azami.event
	async def on_member_remove(member):
		print(f"{member} has left/kick the server")


def main():
	commands_azami()
	event_azami()
	azami.run(os.environ['DISCORD_TOKEN'])
	#token = open("token.txt", "r")
	#azami.run(token.read())

