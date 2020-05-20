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
				embed = discord.Embed(
					title = "Dodged it!",
					description = f"You attempted to shoot me, {ctx.author.mention}, but I dodged it!",
					colour = discord.Color.blue())
				embed.set_image(url = "http://i.imgur.com/hPL5TGD.gif")
				await ctx.send(embed=embed)
				'''
				await ctx.send(
					randomimg.shoot(1) + f"\nYou attempted to shoot me, {ctx.author.mention}, but I dodged it!")
				'''
			'''
			elif member == ctx.author:
				gif = await util.get_file("https://media.giphy.com/media/5xaOcLAo1Gg0oRgBz0Y/giphy.gif")
				await ctx.send(
					f"{ctx.author.name} committed suicide!",
					file = discord.File(io.BytesIO(gif), filename = "gif.gif"))
			else:
				gif = await util.get_file("https://s-media-cache-ak0.pinimg.com/originals/2d/fa/a9/2dfaa995a09d81a07cad24d3ce18e011.gif")
				await ctx.send(f"{member.name} was shot dead by the mighty {ctx.author.name}",
					file = discord.File(io.BytesIO(gif), filename = "gif.gif"))
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