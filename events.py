import discord, os
from discord.ext import commands

azami = commands.Bot(command_prefix = 'a!')

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

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		azami.load_extension(f'cogs.{filename[:-3]}')
		print(f"The following cog has loaded: {filename[:-3]}")


def commands_azami():
	
	@azami.command()
	async def hello(ctx):
		await ctx.send(f"Hello!, {ctx.author.mention}")

	@azami.command()
	async def ping(self, ctx):
		await ctx.send(f'Pong! :ping_pong: {round(azami.latency * 1000)}ms.')

	def to_upper(argument):
		return argument.upper()

	@azami.command()
	async def up(ctx, *, content: to_upper):
		await ctx.send(content)

	@azami.command()
	async def clear(ctx, amount = 5):
		await ctx.channel.purge(limit = amount + 1)

def event_azami():

	@azami.event
	async def on_ready():
		await azami.change_presence(status=discord.Status.online, activity=discord.Game("I'm alive!"))
		print("We have logged in as {0.user}".format(azami))

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

