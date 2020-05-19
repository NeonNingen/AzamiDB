import discord, os
from discord.ext import commands
from random import choice, randint
from random_images import *

azami = commands.Bot(command_prefix = 'a!')

@azami.command()
async def load(ctx, extension):
	azami.load_extension(f'cogs.{extension}', ctx)

@azami.command()
async def unload(ctx, extension):
	azami.unload_extension(f'cogs.{extension}', ctx)

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		azami.load_extension(f'cogs.{filename[:-3]}')


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
		await ctx.send(slap_images() + '\n' + '{0.author.mention} slapped {1}'.format(ctx, user))
	
	@azami.command()
	async def hello(ctx):
		await ctx.send(f"Hello!, {ctx.author.mention}")

	@azami.command()
	async def add(ctx, a: float, b: float):
		await ctx.send(f"{a} + {b} = {a + b}")

	@azami.command(aliases = ['takeaway'])
	async def subtract(ctx, a: float, b: float):
		await ctx.send(f"{a} - {b} = {a - b}")

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

	@azami.command()
	@commands.has_permissions(kick_members = True)
	async def kick(ctx, member: discord.Member, *, reason=None):
		await member.kick(reason=reason)
		await ctx.send(f"You have kicked, {member.mention}")

	@azami.command(ban_members = True)
	@commands.has_permissions(ban_members = True)
	async def ban(ctx, member: discord.Member, *, reason=None):
		await member.ban(reason=reason)
		await ctx.send(f"You have banned, {member.mention}")

	@azami.command(ban_members = True)
	@commands.has_permissions(ban_members = True)
	async def unban(ctx, *, member):
		banned_users = await ctx.guild.bans()
		member_name, member_discriminator = member.split('#')

		for ban_entry in banned_users:
			user = ban_entry.user

			if(user.name, user.discriminator) == (member_name, member_discriminator):
				await ctx.guild.unban(user)
				await ctx.send(f'You have unbanned, {user.mention}')
				return

	

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
		await ctx.channel.purge(limit = amount + 1)

def event_azami():

	@azami.event
	async def on_ready():
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

