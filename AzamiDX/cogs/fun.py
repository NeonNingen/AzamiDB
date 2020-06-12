import discord, io
from discord.ext import commands
from random import choice, randint
from asyncio import sleep
from AzamiDX.core.utils import pre_embed, edit
from AzamiDX.etc.etccont.color_str_embed import return_color_str_to_color_emb
from AzamiDX.etc.fun import randomimg


def to_upper(argument):
	return argument.upper()

class Fun(commands.Cog):

	def __init__(self, azami):
		self.azami = azami

	class Slapper(commands.Converter):
		async def convert(self, ctx, argument):
			to_slap = choice(ctx.guild.members)
			return f'{ctx.author} slapped {to_slap} because *{argument}*'

	@commands.command(description="It's your fault!")
	async def blame(self, ctx, *, reason: Slapper):
		await edit(ctx, content=reason)

	@commands.command(description='This is gonna hurt!')
	async def slap(self, ctx, user):
		embed = discord.Embed(
			title = "That hurts!",
			description = f"{ctx.author.mention} slapped {user}",
			colour = discord.Color.dark_red())
		embed.set_image(url = randomimg.slap())
		await edit(ctx, embed=embed)

	@commands.command(name='8 or 8ball', aliases=['8ball', '8'], 
					  description='What answers do you seek?',
					  usage='Have your questions answered!')
	async def _8ball(self, ctx, *, question):
		with open('AzamiDX/etc/fun/responses_fun.txt', 'r') as f:
			responses = f.read().splitlines()
			
		await edit(ctx, content=f"Questions: {question}\nAnswer: {choice(responses)}")

	@commands.command(description='azami -> AZAMI',
					  usage='Basically capitalizes anything you say')
	async def up(self, ctx, *, content: to_upper):
		await edit(ctx, content=content)

	@commands.command(description='Bang and the dirt is gone',
					  usage='You can suicide, shoot others or shoot Azami!')
	async def shoot(self, ctx, *members: discord.Member):
		if not members: # Built in error check
			await edit(ctx, content="You gotta give me someone to shoot!")
			return
		for member in members:
			if member == self.azami.user:
				embed = discord.Embed(
					title = "Dodged it!",
					description = f"You attempted to shoot me {ctx.author.mention}, but I dodged it!",
					colour = discord.Color.green())
				embed.set_image(url = randomimg.shoot(1))
				await edit(ctx, embed=embed)
			elif member == ctx.author:
				embed = discord.Embed(
					title = "You died! Better luck next time!",
					description = f"{ctx.author.name} committed suicide!",
					colour = discord.Color.red())
				embed.set_image(url = randomimg.shoot(2))
				await edit(ctx, embed=embed)
			else:
				embed = discord.Embed(
					title = "It's a hit!",
					description = f"{member.name} was shot dead by the mighty {ctx.author.name}",
					colour = discord.Color.gold())
				embed.set_image(url = randomimg.shoot(3))
				await edit(ctx, embed=embed)

	@commands.command(description='And your next line is!')
	async def say(self, ctx, *, content):
		await edit(ctx, content=content)

	@commands.command(name="1h",
					  description='Used as a hour reminder')
	async def _1h(self, ctx):
		msg = await ctx.send("Oki see you in an hour!")
		await sleep(3600)
		await msg.delete()
		await ctx.send(f"{ctx.message.author.mention}, an hour is up!")

	@commands.command(description='Nice avatar bro')
	async def avatar(self, ctx, *, user: discord.User):
		em = await pre_embed(titl=f"{user.name}'s avatar",
					   		 desc="I hope they don't mind!",
					   		 color=None,
					   		 image_url=f'{user.avatar_url}',
					   		 ctx=ctx)
		await edit(ctx, embed=em)

	@commands.command(description="Let's play a game of Jan Ken Pon!",
					  aliases=['rockpaperscissors', 'rock'])
	async def rps(self, ctx):
		with open('AzamiDX/etc/fun/url_fun.txt', 'r') as f:
			url = f.read().splitlines()
		hello_em = discord.Embed(title=f"Hello {ctx.message.author.name}",
								 description="Let's play Rock, paper, scissors!",
								 color=discord.Color.green())
		hello_em.set_image(url=f'{url[0]}')
		hello_em.set_thumbnail(url=ctx.message.author.avatar_url)
		hello_em.set_footer(text="Your opponent is me!",
							   icon_url=self.azami.user.avatar_url)
		msg = await ctx.send(embed=hello_em)


		wins = 0
		losses = 0
		ties = 0

		user_rock_em = discord.Embed(title="You threw out a rock",
									 description="Rock against...",
									 color=discord.Color.greyple())
		user_rock_em.set_image(url=f"{url[1]}")
		user_rock_em.set_thumbnail(url=ctx.message.author.avatar_url)

		user_pap_em = discord.Embed(title="You hit me with paper",
									 description="Paper against...",
									 color=discord.Color.teal())
		user_pap_em.set_image(url=f"{url[2]}")
		user_pap_em.set_thumbnail(url=ctx.message.author.avatar_url)
		
		user_sci_em = discord.Embed(title="You slashed out some scissors",
									 description="Scissors against...",
									 color=discord.Color.red())
		user_sci_em.set_image(url=f"{url[3]}")
		user_sci_em.set_thumbnail(url=ctx.message.author.avatar_url) 

		comp_rock_em = discord.Embed(title="Rock!",
									 color=discord.Color.greyple())
		comp_rock_em.set_image(url=f"{url[4]}")
		comp_rock_em.set_thumbnail(url=self.azami.user.avatar_url)

		comp_pap_em = discord.Embed(title="Paper!",
									 color=discord.Color.teal())
		comp_pap_em.set_image(url=f"{url[5]}")
		comp_pap_em.set_thumbnail(url=self.azami.user.avatar_url)

		comp_sci_em = discord.Embed(title="Scissors!",
									 color=discord.Color.red())
		comp_sci_em.set_image(url=f"{url[6]}")
		comp_sci_em.set_thumbnail(url=self.azami.user.avatar_url)

		you_win_em = discord.Embed(title="Congrats you win!",
									 description="I'll get you next time!",
									 color=discord.Color.gold())
		you_win_em.set_image(url=f"{url[7]}")
		you_win_em.set_thumbnail(url=ctx.message.author.avatar_url)

		you_lose_em = discord.Embed(title="Better luck next time!",
									 description="Ha! You lost!",
									 color=discord.Color.dark_red())
		you_lose_em.set_image(url=f"{url[8]}")
		you_lose_em.set_thumbnail(url=self.azami.user.avatar_url)

		tie_em = discord.Embed(title="It's a tie...",
									 description="Prepare to lose next time!",
									 color=discord.Color.purple())
		tie_em.set_image(url=f"{url[9]}")
		tie_em.set_thumbnail(url=ctx.message.author.avatar_url)

		while True:
			await ctx.send(f'Wins: {wins}, Losses: {losses}, Ties: {ties}', delete_after=5)
			while True:
				def check(m):
					return m.author == ctx.author and m.channel == ctx.channel
				msg2 = await ctx.send("What do you choose (r)ock, (p)aper, (s)cissors or (q)uit")
				player = await self.azami.wait_for('message', check=check)
				if player.content == 'q':
					await ctx.send("See you next time")
					return
				if player.content == 'r' or player.content == 'p' or player.content == 's':
					break
				await edit(ctx, content='Write r, p, s or q!', ttl=5)

			if player.content == 'r':
				await player.delete()
				await msg2.delete()
				await msg.edit(embed=user_rock_em)
			elif player.content == 'p':
				await player.delete()
				await msg2.delete()
				await msg.edit(embed=user_pap_em)
			elif player.content == 's':
				await player.delete()
				await msg2.delete()
				await msg.edit(embed=user_sci_em)

			randomnum = randint(1, 3)
			if randomnum == 1:
				computer = 'r'
				await sleep(3)
				await msg.edit(embed=comp_rock_em)
			elif randomnum == 2:
				computer = 'p'
				await sleep(3)
				await msg.edit(embed=comp_pap_em)
			elif randomnum == 3:
				computer = 's'
				await sleep(3)
				await msg.edit(embed=comp_sci_em)

			if player.content == computer:
				await ctx.send("Please wait...", delete_after=4)
				await sleep(4)
				await msg.edit(embed=tie_em)
				ties += 1
			elif player.content == 'r' and computer == 's':
				await ctx.send("Please wait...", delete_after=4)
				await sleep(4)
				await msg.edit(embed=you_win_em)
				wins += 1
			elif player.content == 'r' and computer == 'p':
				await ctx.send("Please wait...", delete_after=4)
				await sleep(4)
				await msg.edit(embed=you_lose_em)
				losses += 1
			elif player.content == 'p' and computer == 'r':
				await ctx.send("Please wait...", delete_after=4)
				await sleep(4)
				await msg.edit(embed=you_win_em)
				wins += 1
			elif player.content == 'p' and computer == 's':
				await ctx.send("Please wait...", delete_after=4)
				await sleep(4)
				await msg.edit(embed=you_lose_em)
				losses += 1
			elif player.content == 's' and computer == 'p':
				await ctx.send("Please wait...", delete_after=4)
				await sleep(4)
				await msg.edit(embed=you_win_em)
				wins += 1
			elif player.content == 's' and computer == 'r':
				await ctx.send("Please wait...", delete_after=4)
				await sleep(4)
				await msg.edit(embed=you_lose_em)
				losses += 1

	@commands.command(aliases=['me'], description="Make your own custom embed!")
	async def makeembed(self, ctx): # Add parameters in the future 1 for like 1 add field
		await edit(ctx, content="Welcome to custom embed maker!", ttl=5)
		await edit(ctx, content="Please follow each instuction to make your own embed!", ttl=10)
		await edit(ctx, content="IMPORTANT: Make sure your url ends with .png, .jpg or .gif", ttl=20)
		while True:
			while True:
				def check(m):
					return m.author == ctx.author and m.channel == ctx.channel
				msg = await ctx.send("Please enter your title",)
				player = await self.azami.wait_for('message', check=check)
				title = player.content
				await player.delete()
				await msg.delete()
				msg = await ctx.send("Please enter your description",)
				player = await self.azami.wait_for('message', check=check)
				desc = player.content
				await player.delete()
				await msg.delete()
				msg = await ctx.send("Please enter your colour of choice",)
				msg2 = await ctx.send("Make sure it is like discord.Color.red()",)
				msg3 = await ctx.send("Or you can just write None for a random one",)
				player = await self.azami.wait_for('message', check=check)
				color = player.content
				if color == "None":
					color = None
				color = return_color_str_to_color_emb(color)
				await player.delete()
				await msg.delete()
				await msg2.delete()
				await msg3.delete()
				msg = await ctx.send("Please enter your thumbnail url",)
				msg2 = await ctx.send("If you don't want a url for this or the next urls"\
										 " write None",)
				player = await self.azami.wait_for('message', check=check)
				thumb_url = player.content
				if thumb_url == "None":
					thumb_url = ""
				await player.delete()
				await msg.delete()
				await msg2.delete()
				msg = await ctx.send("Please enter your image url",)
				player = await self.azami.wait_for('message', check=check)
				image_url = player.content
				if image_url == "None":
					image_url = ""
				await player.delete()
				await msg.delete()
				msg = await ctx.send("Please enter your footer text",)
				msg2 = await ctx.send("If you don't want a footer text for this or the next urls"\
										 " write None",)
				player = await self.azami.wait_for('message', check=check)
				foot_txt = player.content
				if foot_txt == "None":
					foot_txt = ""
				await player.delete()
				await msg.delete()
				await msg2.delete()
				msg = await ctx.send("Please enter your footer avatar url",)
				player = await self.azami.wait_for('message', check=check)
				foot_url = player.content
				if foot_url == "None":
					foot_url = ""
				await player.delete()
				await msg.delete()
				msg = await ctx.send("Please Wait")
				await sleep(2)
				await msg.delete()
				break
			break

		em = await pre_embed(titl=title,
					   		 desc=desc,
					   		 color=color,
					   		 thumb_url=thumb_url,
					   		 image_url=image_url,
					   		 text_em=foot_txt,
					   		 foot_url=foot_url,
					   		 ctx=ctx)
		try:
			await edit(ctx, embed=em)
		except:
			color = None
			thumb_url = ''
			image_url = ''
			foot_url = ''
			em = await pre_embed(titl=title,
								 desc=desc,
								 color=color,
								 thumb_url=thumb_url,
								 image_url=image_url,
								 text_em=foot_txt,
								 foot_url=foot_url,
								 ctx=ctx)
			await edit(ctx, embed=em)
			await edit(ctx, content="There was an error in the URL(s). " \
									"Recommend you put None when asked " \
									"for the URL(s)")

	@avatar.error
	async def avatar_error(self, ctx, error):
		if isinstance(error, commands.BadArgument):
			em = await pre_embed(titl="User not found",
								 desc="This person is not in the current guild",
								 color=discord.Color.red(),
								 ctx=ctx)
			await edit(ctx, embed=em)
	

def setup(azami):
	azami.add_cog(Fun(azami))