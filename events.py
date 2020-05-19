import discord, os
from discord.ext import commands
from random import choice, randint
from random_images import *

azami = commands.Bot(command_prefix = 'a!')

def commands_azami():

	class Slapper(commands.Converter):
		async def convert(self, ctx, argument):
			to_slap = choice(ctx.guild.members)
			return '{0.author} slapped {1} because *{2}*'.format(ctx, to_slap, argument)

	@azami.command()
	async def blame(ctx, *, reason: Slapper):
		await ctx.send(reason)

	@azami.command()
	async def slap(ctx, user):
		await ctx.send(slap_images() + '\n' + '{0.author} slapped {1}'.format(ctx, user))

	@azami.command()
	async def ping(ctx):
		await ctx.send(f'Pong! :ping_pong: {round(azami.latency * 1000)}ms.')

	@azami.command()
	async def hello(ctx):
		await ctx.send("Hello!, {0.author}".format(ctx))

	@azami.command()
	async def add(ctx, a: float, b: float):
		await ctx.send(a + b)

	@azami.command(aliases = ['takeaway'])
	async def subtract(ctx, a: float, b: float):
		await ctx.send(a - b)

	@azami.command(aliases = ['times'])
	async def multiply(ctx, a: float, b: float):
		await ctx.send(a * b)

	@azami.command(aliases = ['division'])
	async def divide(ctx, a: float, b: float):
		await ctx.send(a / b)

	@azami.command()
	async def d4(ctx):
		await ctx.send(f"You rolled: {randint(1, 4)}")

	@azami.command()
	async def d6(ctx):
		await ctx.send(f"You rolled: {randint(1, 6)}")

	@azami.command()
	async def d8(ctx):
		await ctx.send(f"You rolled: {randint(1, 8)}")

	@azami.command()
	async def d10(ctx):
		await ctx.send(f"You rolled: {randint(1, 10)}")

	@azami.command()
	async def d100(ctx):
		await ctx.send(f"You rolled: {randint(1, 100)}")

	@azami.command()
	async def d12(ctx):
		await ctx.send(f"You rolled: {randint(1, 12)}")

	@azami.command()
	async def d20(ctx):
		await ctx.send(f"You rolled: {randint(1, 20)}")

	
	

	def to_upper(argument):
		return argument.upper()

	@azami.command()
	async def up(ctx, *, content: to_upper):
		await ctx.send(content)

	@azami.command(aliases=['8ball', '8'])
	async def _8ball(ctx, *, question):
		responses = ["It is certain.",
					"It is decidedly so.",
        			"Without a doubt.",
        			"Yes - definitely.",
        			"You may rely on it.",
        			"As I see it, yes.",
        			"Most likely.",
        			"Outlook good.",
        			"Yes.",
        			"Signs point to yes.",
        			"Reply hazy, try again.",
        			"Ask again later.",
        			"Better not tell you now.",
        			"Cannot predict now.",
        			"Concentrate and ask again.",
        			"Don't count on it.",
        			"My reply is no.",
        			"My sources say no.",
        			"Outlook not so good.",
        			"Very doubtful."]
		await ctx.send("Questions: {0}\nAnswer: {1}".format(question, choice(responses)))

	@azami.command()
	async def clear(ctx, amount = 5):
		await ctx.channel.purge(limit = amount)

def event_azami():

	@azami.event
	async def on_ready():
		print("We have logged in as {0.user}".format(azami))

	@azami.event
	async def on_member_join(member):
		print("{0.member} has joined the server".format(member))

	@azami.event
	async def on_member_remove(member):
		print("{0.member} has left/kick the server".format(member))


def main():
	commands_azami()
	event_azami()
	azami.run(os.environ['DISCORD_TOKEN'])
	#token = open("token.txt", "r")
	#azami.run(token.read())

