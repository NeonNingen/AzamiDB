import discord, io, re
from discord.ext import commands
from random import choice, randint
from asyncio import sleep, TimeoutError
from AzamiDX.core.utils import color_list, edit, pre_embed
from AzamiDX.etc.fun import randomimg, funembed

def to_upper(argument):
	return argument.upper()

class Fun(commands.Cog):

	def __init__(self, azami): # Marriage command add
		self.azami = azami
		self.timer_arr = []

	@commands.command(description='This is gonna hurt!')
	async def slap(self, ctx, *members: discord.Member):
		exit = await self.azami.restrictor(ctx)
		if exit == True: return

		if not members: # Built in error check
			await ctx.send("You gotta give me someone to slap!")
			return

		slapped = funembed.slapper(ctx)
		key2 = randint(1, 2)

		for member in members:
			if member == self.azami.user:
				em = await pre_embed(titl=slapped['azami'][key2]['title'],
									 desc=slapped['azami'][key2]['desc'],
									 color=slapped['azami'][1]['color'],
									 image_url=slapped['azami'][key2]['url'])
			elif member == ctx.author:
				em = await pre_embed(titl=slapped['self'][key2]['title'],
									 desc=slapped['self'][key2]['desc'],
									 color=slapped['self'][1]['color'],
									 image_url=slapped['self'][key2]['url'])
			else:
				em = await pre_embed(titl=slapped['others']['title'],
									 desc=slapped['others']['desc'],
									 image_url=slapped['others']['url'])
			await edit(ctx, embed=em)

		self.azami.id_store.remove(ctx.message.author.id)

	@commands.command(description='azami -> AZAMI',
					  usage='Basically capitalizes anything you say')
	async def up(self, ctx, *, content: to_upper):
		await edit(ctx, content=content)

	@commands.command(description='Bang and the dirt is gone',
					  usage='You can suicide, shoot others or shoot Azami!')
	async def shoot(self, ctx, *members: discord.Member):
		exit = await self.azami.restrictor(ctx)
		if exit == True: return

		if not members:
			await edit(ctx, content="You gotta give me someone to shoot!")
			return

		for member in members:
			shooter = funembed.shoot(member, ctx)
			if member == self.azami.user:
				em = await pre_embed(titl=shooter['azami']['title'],
									 desc=shooter['azami']['desc'],
									 color=shooter['azami']['color'],
									 image_url=shooter['azami']['url'])
			elif member == ctx.author:
				em = await pre_embed(titl=shooter['self']['title'],
									 desc=shooter['self']['desc'],
									 color=shooter['self']['color'],
									 image_url=shooter['self']['url'])
			else:
				em = await pre_embed(titl=shooter['others']['title'],
									 desc=shooter['others']['desc'],
									 image_url=shooter['others']['url'])
			await edit(ctx, embed=em)

		self.azami.id_store.remove(ctx.message.author.id)

	@commands.command(description='And your next line is!')
	async def say(self, ctx, *, content):
		exit = await self.azami.restrictor(ctx)
		if exit == True: return

		await ctx.send(content)
		self.azami.id_store.remove(ctx.message.author.id)

	@commands.command(description='Kinda self explanatory, read usage on how to use',
					  usage='Format: `a!timer NhNmNs` replace N with the desired number')
	async def timer(self, ctx, time: str):
		id_list = set(self.timer_arr)
		if ctx.message.author.id in id_list:
			await ctx.send("You already have set up a timer", delete_after=5)
			return
		else:
			try:
				time = re.split('h|m|s', time)
				timecheck = int(time[0] + time[1] + time[2])
				msg = await ctx.send(f"Timer to set off in **{time[0]}** hour(s)" \
								 	 f", **{time[1]}** minute(s) and **{time[2]}** second(s)")
				self.timer_arr.append(ctx.message.author.id)
				await sleep((int(time[0]) * 3600) + (int(time[1]) * 60) + (int(time[2])))
				await ctx.send(f"{ctx.message.author.mention}, time is up!")
				await msg.delete()
				self.timer_arr.remove(ctx.message.author.id)
			except Exception:
				await ctx.send('The format has to be in NhNNmNs!', delete_after=5)

	@commands.command(description='Nice avatar bro')
	async def avatar(self, ctx, *, user: discord.User):
		exit = await self.azami.restrictor(ctx)
		if exit == True: return

		em = await pre_embed(titl=f"{user.name}'s avatar",
					   		 desc="I hope they don't mind!",
					   		 color=None,
					   		 image_url=f'{user.avatar_url}',
					   		 ctx=ctx)
		await edit(ctx, embed=em)
		self.azami.id_store.remove(ctx.message.author.id)

	@commands.command(description="Let's play a game of Jan Ken Pon!")
	async def rps(self, ctx):
		exit = await self.azami.restrictor(ctx)
		if exit == True: return

		def check(m):
			return m.author == ctx.author and m.channel == ctx.channel and m.content.lower() in ['r', 'p', 's', 'q']

		wins = 0
		losses = 0
		ties = 0

		rpsci = funembed.rockpapsci(ctx)

		
		em = discord.Embed(title=rpsci['default']['title'],
						   description=rpsci['default']['desc'],
						   color=color_list())
		em.set_image(url=rpsci['default']['url'])
		em.set_thumbnail(url=ctx.message.author.avatar_url)
		em.set_footer(text=rpsci['default']['footer'])

		msg = await ctx.send(embed=em)
		
		while True:
			rpsci = funembed.rockpapsci(ctx)
			em = discord.Embed(title="What do you choose (r)ock, (p)aper, (s)cissors or (q)uit")
			choicemsg = await ctx.send(embed=em)

			try:
				player = await self.azami.wait_for('message', check=check, timeout=120)
				if player.content == 'q':
					self.azami.id_store.remove(ctx.message.author.id)
					await ctx.send("See you next time!")
					return

			except TimeoutError:
				await ctx.send('Timed out')
				self.azami.id_store.remove(ctx.message.author.id)
				return

			await choicemsg.delete()
			em = discord.Embed(title=rpsci[player.content][1]['title'],
						   description=rpsci[player.content][1]['desc'])
			em.set_image(url=rpsci[player.content][1]['url'])
			await msg.edit(embed=em)
			await sleep(3)

			comp = choice(['r', 'p', 's'])

			em = discord.Embed(title=rpsci[comp][2]['title'],
							   description="Please wait....",
							   color=rpsci[comp][1]['color'])
			em.set_image(url=rpsci[comp][2]['url'])
			await msg.edit(embed=em)

			if player.content == comp:
				em = discord.Embed(title=rpsci['end']['tie']['title'],
								   color=rpsci['end']['tie']['color'])
				em.set_image(url=rpsci['end']['tie']['url'])
				ties += 1

			elif rpsci[player.content][1]['beats'] == comp:
				em = discord.Embed(title=rpsci['end']['winner']['title'],
							   	   color=rpsci['end']['winner']['color'])
				em.set_image(url=rpsci['end']['winner']['url'])
				em.set_thumbnail(url=ctx.message.author.avatar_url)
				wins += 1

			else:
				em = discord.Embed(title=rpsci['end']['loser']['title'],
								   color=rpsci['end']['loser']['color'])
				em.set_image(url=rpsci['end']['loser']['url'])
				em.set_thumbnail(url=self.azami.user.avatar_url)
				losses += 1
			
			em.set_footer(text=f'Wins: {wins} | Losses: {losses} | Ties: {ties}')
			await sleep(4)
			await player.delete()
			await msg.edit(embed=em)

	@commands.command(name='8ball', aliases=['8'], 
					  description='What answers do you seek?',
					  usage='Have your questions answered!')
	async def _8ball(self, ctx, *, question):
		exit = await self.azami.restrictor(ctx)
		if exit == True: return
		with open('AzamiDX/etc/fun/responses_fun.txt', 'r') as f:
			responses = f.read().splitlines()
			
		await ctx.send(ctx, content=f"Questions: {question}\nAnswer: {choice(responses)}")

		self.azami.id_store.remove(ctx.message.author.id)

	@commands.command(aliases=['me'], description="Make your own custom embed!")
	async def makeembed(self, ctx):
		exit = await self.azami.restrictor(ctx)
		if exit == True: return

		def check(m):
			return m.author == ctx.author and m.channel == ctx.channel

		def intcheck(m):
			return m.author == ctx.author and m.channel == ctx.channel and type(int(m.content)) == int

		member = ctx.message.author
		me = funembed.customem(ctx)
		emoji_list = [['Title', '1⃣'], ['Description', '2⃣'], ['Color', '3⃣'],
					 ['Thumbnail', '4⃣'], ['Image', '5⃣'], ['Footer Text', '6⃣'],
					 ['Footer Image', '7⃣'], ['Fields', '8⃣'], ['Finished', '9⃣'], 
					 ['Quit', '0⃣']]

		list_var = {}

		field_name = []
		field_value = []

		em = discord.Embed(title=f"Welcome to custom embed marker {ctx.message.author.name}!",
						   description="Please press on a reaction to edit a certain part of your own embed\n"\
						   			   "IMPORTANT: Make sure your url ends with .png, .jpg, .webm or .gif",
						   color=color_list())

		for i in range(0, 10):
			em.add_field(name=emoji_list[i][0], value=emoji_list[i][1])
		message = await ctx.send(embed=em)
		for i in range(0, 10):
			await message.add_reaction(emoji_list[i][1])

		while True:
			try:
				reaction, user = await self.azami.wait_for('reaction_add', timeout=120, check=lambda r, u: member)
			except TimeoutError:
				await ctx.send("Timed out")
				return

			for i in range(0, 7):
				if str(reaction) == str(emoji_list[i][1]) and user == member:

					await message.remove_reaction(str(reaction), user)
					em = discord.Embed(title=me[str(reaction)]['title'],
									   description=me[str(reaction)]['desc'])
					em.set_image(url=me[str(reaction)]['url'])
					new_em = await ctx.send(embed=em)

					try:
						player = await self.azami.wait_for('message', check=check, timeout=120)
						list_var[str(reaction)] = player.content
						await new_em.delete()
						await player.delete()
					except TimeoutError:
						await ctx.send("Timed out")
						return

			if str(reaction) == str(emoji_list[9][1]) and user == member:
				await ctx.send("Custom Embed has ended")
				self.azami.id_store.remove(ctx.message.author.id)
				return

			if str(reaction) == str(emoji_list[8][1]) and user == member:
				self.azami.id_store.remove(ctx.message.author.id)
				await message.delete()
				em = await funembed.final_embed(ctx, list_var, field_name, field_value)
				await edit(ctx, embed=em)
				return

			if str(reaction) == str(emoji_list[7][1]) and user == member:
				await message.remove_reaction(str(reaction), user)
				em = discord.Embed(title=me[str(reaction)]['title'],
									   description=me[str(reaction)]['desc'])
				em.set_image(url=me[str(reaction)]['url'])
				new_em = await ctx.send(embed=em)

				list_var[str(reaction)] = ""

				try:
					player = await self.azami.wait_for('message', check=intcheck, timeout=120)
					num = int(player.content)
					await player.delete()
				except ValueError:
					await ctx.send("Incorrect Value, Leaving Field.", timeout=5)
					num = 0
				except TimeoutError:
					await ctx.send("Timed out")
					return

				em = discord.Embed(title=f'Please enter {num} title(s) for each field')
				await new_em.edit(embed=em)

				for i in range(0, num):
					count = await ctx.send(f'Title {i+1}')
					try:
						player = await self.azami.wait_for('message', check=check, timeout=120)
						field_name.append(player.content)
						await player.delete()
						await count.delete()
					except TimeoutError:
						await ctx.send("Timed out")
						return

				em = discord.Embed(title=f'Please enter {num} description(s) for each field')
				await new_em.edit(embed=em)

				for i in range(0, num):
					count = await ctx.send(f'Description {i+1}')
					try:
						player = await self.azami.wait_for('message', check=check, timeout=120)
						field_value.append(player.content)
						await player.delete()
						await count.delete()
					except TimeoutError:
						await ctx.send("Timed out")
						return

				await new_em.delete()

	class Slapper(commands.Converter):
		async def convert(self, ctx, argument):
			to_slap = choice(ctx.guild.members)
			return f'{ctx.author} slapped {to_slap} because *{argument}*'

	@commands.command(description="It's your fault!")
	async def blame(self, ctx, *, reason: Slapper):
		exit = await self.azami.restrictor(ctx)
		if exit == True:
			return
		await edit(ctx, content=reason)
		self.azami.id_store.remove(ctx.message.author.id)

	@avatar.error
	async def avatar_error(self, ctx, error):
		if isinstance(error, commands.BadArgument):
			em = await pre_embed(titl="User not found",
								 desc="This person is not in the current guild",
								 color=discord.Color.red(),
								 ctx=ctx)
			await edit(ctx, embed=em)
			self.azami.id_store.remove(ctx.message.author.id)

	@makeembed.error
	async def makeembed_error(self, ctx, error):
			em = await pre_embed(titl='An Error Occured',
								 desc=f"{error}",
								 color=discord.Color.red(),
								 ctx=ctx)
			await edit(ctx, embed=em)
			self.azami.id_store.remove(ctx.message.author.id)
	

def setup(azami):
	azami.add_cog(Fun(azami))