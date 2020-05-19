import discord, sys
from discord.ext import commands
from random import choice, randint
sys.path.insert(1, '../')
from random_images import *

def to_upper(argument):
	return argument.upper()

class Fun(commands.Cog):

	def __init__(self, azami):
		self.azami = azami

	class Slapper(commands.Converter):
		async def convert(self, ctx, argument):
			to_slap = choice(ctx.guild.members)
			return '{0.author} slapped {1} because *{2}*'.format(ctx, to_slap, argument)

	@commands.command()
	async def blame(self, ctx, *, reason: Slapper):
		await ctx.send(reason)

	@commands.command()
	async def slap(self, ctx, user):
		await ctx.send(slap_images() + '\n' + '{0.author.mention} slapped {1}'.format(ctx, user))

	@commands.command(aliases=['8ball', '8'])
	async def _8ball(self, ctx, *, question):
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

	@commands.command()
	async def up(self, ctx, *, content: to_upper):
		await ctx.send(content)
	

def setup(azami):
	azami.add_cog(Fun(azami))