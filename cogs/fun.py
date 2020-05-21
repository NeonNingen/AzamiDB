import discord, sys, io
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument
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
			return f'{ctx.author} slapped {to_slap} because *{argument}*'

	@commands.command()
	async def blame(self, ctx, *, reason: Slapper):
		await ctx.send(reason)

	@commands.command()
	async def slap(self, ctx, user):
		embed = discord.Embed(
			title = "That hurts!",
			description = f"{ctx.author.mention} slapped {user}",
			colour = discord.Color.dark_red())
		embed.set_image(url = randomimg.slap())
		await ctx.send(embed=embed)

	@commands.command(aliases=['8ball', '8'])
	async def _8ball(self, ctx, *, question):
		with open('responses_fun.txt', 'r') as f:
			responses = f.read().splitlines()
			# When rehauling use folders for each cog
		await ctx.send(f"Questions: {question}\nAnswer: {choice(responses)}")

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
					description = f"You attempted to shoot me {ctx.author.mention}, but I dodged it!",
					colour = discord.Color.green())
				embed.set_image(url = randomimg.shoot(1))
				await ctx.send(embed=embed)
			elif member == ctx.author:
				embed = discord.Embed(
					title = "You died! Better luck next time!",
					description = f"{ctx.author.name} committed suicide!",
					colour = discord.Color.red())
				embed.set_image(url = randomimg.shoot(2))
				await ctx.send(embed=embed)
			else:
				embed = discord.Embed(
					title = "It's a hit!",
					description = f"{member.name} was shot dead by the mighty {ctx.author.name}",
					colour = discord.Color.gold())
				embed.set_image(url = randomimg.shoot(3))
				await ctx.send(embed=embed)
	

	@slap.error # Find out how to remove error from console
	async def slap_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument):
			await ctx.send("Requires an user to hit")
			return
		return error

	@_8ball.error
	async def ball8_error(self, ctx, error):
		if isinstance(error, MissingRequiredArgument):
			await ctx.send("Requires an argument")
			return
		return error
	

def setup(azami):
	azami.add_cog(Fun(azami))