import discord, os, random
from discord.ext import commands, tasks
from discord.ext.commands import CommandNotFound
from itertools import cycle

azami = commands.Bot(command_prefix = 'a!',
					 description = "Azami, an all purpose bot!",
					 owner_id = 288022950576390144)

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
# Add JoJo Command, fix errors
def commands_azami():
	
	@azami.command()
	async def hello(ctx):
		await ctx.send(f"Hello!, {ctx.author.mention}")

	@azami.command()
	async def ping(ctx):
		await ctx.send(f'Pong! :ping_pong: {round(azami.latency * 1000)}ms.')

	@azami.command()
	async def clear(ctx, amount: int = 5):
		await ctx.channel.purge(limit = amount + 1)

	@azami.command()
	async def invite(ctx):
		await ctx.send("The server invite: https://discord.gg/rRb23dt")


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
		print(f"{member} has left/kick from the server")

	@azami.event
	async def on_command_error(ctx, error):
		if isinstance(error, CommandNotFound):
			await ctx.send("Invalid command, did you type that right?")
			return
		raise error

def main():
	commands_azami()
	event_azami()
	azami.run(os.environ['DISCORD_TOKEN'])
	#token = open("token.txt", "r")
	#azami.run(token.read())

