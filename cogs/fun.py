import discord, sys, io
from discord.ext import commands
from random import choice, randint
sys.path.insert(1, '../')
import randomimg

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
		await ctx.send(randomimg.slap() + '\n' + '{0.author.mention} slapped {1}'.format(ctx, user))

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

	@commands.command()
	async def shoot(self, ctx, *members: discord.Member):
		if not members: # Built in error check
			await ctx.send("You gotta give me someone to shoot!")
			return
		for member in members:
			if member == self.azami.user:
				embed = discord.Embed(title="Title", description="Desc", color=0x00ff00)
				file = discord.File("gifs/shoot_gif1.gif", filename="image.gif")
				embed.set_image(url="attachment://image.gif")
				await ctx.send(
					f"You attempted to shoot me, {ctx.author.name}, but I dodged it!",
					file=file, embed=embed)
		'''		

			elif member == ctx.author:
				await ctx.send(
					f"{ctx.author.name} committed suicide!",
					file = randomimg.shoot(2))
			else:
				await ctx.send(f"{member.name} was shot dead by the mighty {ctx.author.name}",
					file = randomimg.shoot(3))
		'''
	

	@slap.error # Find out how to remove error from console
	async def slap_error(self, ctx, error):
		if isinstance(error, commands.CommandError):
			await ctx.send("Requires an argument")
			return
		return error

	@_8ball.error
	async def ball8_error(self, ctx, error):
		if isinstance(error, commands.CommandError):
			await ctx.send("Requires an argument")
			return
		return error
	

def setup(azami):
	azami.add_cog(Fun(azami))