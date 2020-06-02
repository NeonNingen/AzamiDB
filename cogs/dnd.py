import discord, sys, time
from discord.ext import commands
from random import randint
from asyncio import sleep
sys.path.insert(1, '../')
from diceimg import diceroll

def return_results(limit, rolls, mod, i=0):
	if rolls == 1:
		result = ', '.join(str(randint(1, limit)) for r in range(rolls))
		result = int(result)

		if mod > 0:
			result = result + mod

		result_em = discord.Embed(title=f"Here's your result!",
							  	  description=f"You got: {result}!",
							  	  color=discord.Color.gold())

		if result > 20:
			return result_em
		else:
			dicepic = diceroll(result)
			result_em.set_image(url=dicepic)
			return result_em

	else:
		multi_em = discord.Embed(title=f"Rolled so far {i+1}",
								 color=discord.Color.gold())
		limit = randint(1, limit)

		if mod > 0:
			limit = limit + mod

		if limit > 20:
			return multi_em.add_field(name=f"Roll {i + 1}", value=f"This your value: {limit}")
		else:
			dicepic = diceroll(limit)
			multi_em.add_field(name=f"Roll {i + 1}", value=f"This your value: {limit}")
			multi_em.set_image(url=dicepic)
			return multi_em

class Dnd(commands.Cog): # Work on Embed Rolls also modifier addon

	def __init__(self, azami):
		self.azami = azami

	@commands.command(description=f'The format must be NdN',
					  usage='To roll any dice, any amount of times')
	async def roll(self, ctx, dice: str, mod=0):
		try:
			rolls, limit = map(int, dice.split('d'))
		except Exception:
			await ctx.send('The format has to be in NdN!')
			return

		roll_em = discord.Embed(title=f"Rolling {rolls} dice(s)",
								description=f"Hope you get a natural {limit}!",
								color=discord.Color.teal())
		roll_em.set_thumbnail(url=ctx.message.author.avatar_url)

		if limit == 4:
			roll_em.set_image(url="https://media.giphy.com/media/fiqcUhBNj6jWgJnRlu/giphy.gif")
			roll_em.add_field(name=f"Currently rolling {rolls}d{limit}", value="\u200b")
			msg = await ctx.send(embed=roll_em)
			await sleep(2)
			result_em = return_results(limit, rolls, mod)
			result_em.set_thumbnail(url=ctx.message.author.avatar_url)
			if rolls > 1:
				await msg.delete()
				for i in range(0, rolls):
					result_em = return_results(limit, rolls, mod, i)
					result_em.set_thumbnail(url=ctx.message.author.avatar_url)
					await ctx.send(embed=result_em)
			else:
				await msg.edit(embed=result_em)

		elif limit == 6:
			roll_em.set_image(url="https://bestanimations.com/Games/Dice/rolling-dice-gif-1.gif")
			roll_em.add_field(name=f"Currently rolling {rolls}d{limit}", value="\u200b")
			msg = await ctx.send(embed=roll_em)
			await sleep(2)
			result_em = return_results(limit, rolls, mod)
			result_em.set_thumbnail(url=ctx.message.author.avatar_url)
			if rolls > 1:
				await msg.delete()
				for i in range(0, rolls):
					result_em = return_results(limit, rolls, mod, i)
					result_em.set_thumbnail(url=ctx.message.author.avatar_url)
					await ctx.send(embed=result_em)
			else:
				await msg.edit(embed=result_em)

		elif limit == 8:
			roll_em.set_image(url="https://66.media.tumblr.com/457d10f08e468d1392ab7165ab330ba7/dc90dde4ae909e0f-2b/s400x600/a62e416692fcddf76e7623d560b89a8ad102a5c6.gifv")
			roll_em.add_field(name=f"Currently rolling {rolls}d{limit}", value="\u200b")
			msg = await ctx.send(embed=roll_em)			
			await sleep(2)
			result_em = return_results(limit, rolls, mod)
			result_em.set_thumbnail(url=ctx.message.author.avatar_url)
			if rolls > 1:
				await msg.delete()
				for i in range(0, rolls):
					result_em = return_results(limit, rolls, mod, i)
					result_em.set_thumbnail(url=ctx.message.author.avatar_url)
					await ctx.send(embed=result_em)
			else:
				await msg.edit(embed=result_em)

		elif limit == 10:
			roll_em.set_image(url="https://66.media.tumblr.com/3096dd055c2c00055e68e46695d18b09/23077a30d50cc0d0-93/s400x600/0936ec389211b11f159f79265b15a44370e8688a.gifv")
			roll_em.add_field(name=f"Currently rolling {rolls}d{limit}", value="\u200b")
			msg = await ctx.send(embed=roll_em)
			await sleep(2)
			result_em = return_results(limit, rolls, mod)
			result_em.set_thumbnail(url=ctx.message.author.avatar_url)
			if rolls > 1:
				await msg.delete()
				for i in range(0, rolls):
					result_em = return_results(limit, rolls, mod, i)
					result_em.set_thumbnail(url=ctx.message.author.avatar_url)
					await ctx.send(embed=result_em)
			else:
				await msg.edit(embed=result_em)

		elif limit == 100:
			roll_em.set_image(url="https://i.pinimg.com/originals/2f/d5/73/2fd573b2f3c6499ec3963b77475b43b2.png")
			roll_em.add_field(name=f"Currently rolling {rolls}d{limit}", value="\u200b")
			msg = await ctx.send(embed=roll_em)
			await sleep(2)
			result_em = return_results(limit, rolls, mod)
			result_em.set_thumbnail(url=ctx.message.author.avatar_url)
			if rolls > 1:
				await msg.delete()
				for i in range(0, rolls):
					result_em = return_results(limit, rolls, mod, i)
					result_em.set_thumbnail(url=ctx.message.author.avatar_url)
					await ctx.send(embed=result_em)
			else:
				await msg.edit(embed=result_em)

		elif limit == 12:
			roll_em.set_image(url="https://webstockreview.net/images/dice-clipart-d12-5.png")
			roll_em.add_field(name=f"Currently rolling {rolls}d{limit}", value="\u200b")
			msg = await ctx.send(embed=roll_em)
			await sleep(2)
			result_em = return_results(limit, rolls, mod)
			result_em.set_thumbnail(url=ctx.message.author.avatar_url)
			if rolls > 1:
				await msg.delete()
				for i in range(0, rolls):
					result_em = return_results(limit, rolls, mod, i)
					result_em.set_thumbnail(url=ctx.message.author.avatar_url)
					await ctx.send(embed=result_em)
			else:
				await msg.edit(embed=result_em)

		elif limit == 20:
			roll_em.set_image(url="https://66.media.tumblr.com/1458225a6051e572f34b931011630d71/tumblr_ol1es3Lg4a1tevcm3o1_400.gifv")
			roll_em.add_field(name=f"Currently rolling {rolls}d{limit}", value="\u200b")
			msg = await ctx.send(embed=roll_em)
			await sleep(2)
			result_em = return_results(limit, rolls, mod)
			result_em.set_thumbnail(url=ctx.message.author.avatar_url)
			if rolls > 1:
				await msg.delete()
				for i in range(0, rolls):
					result_em = return_results(limit, rolls, mod, i)
					result_em.set_thumbnail(url=ctx.message.author.avatar_url)
					await ctx.send(embed=result_em)
			else:
				await msg.edit(embed=result_em)

		else:
			roll_em.set_image(url="https://cdn.shopify.com/s/files/1/1483/3510/products/Haunted_Dice_Ice_grande.gif")
			roll_em.add_field(name=f"Currently rolling {rolls}d{limit}", value="\u200b")
			msg = await ctx.send(embed=roll_em)
			await sleep(2)
			result_em = return_results(limit, rolls, mod)
			result_em.set_thumbnail(url=ctx.message.author.avatar_url)
			if rolls > 1:
				await msg.delete()
				for i in range(0, rolls):
					result_em = return_results(limit, rolls, mod, i)
					result_em.set_thumbnail(url=ctx.message.author.avatar_url)
					await ctx.send(embed=result_em)
			else:
				await msg.edit(embed=result_em)

	@commands.command(description='Rolling initiative',
					  usage='This will decide who gets to attack first')
	async def initiative(self, ctx, dice: str):
		try:
			rolls, limit = map(int, dice.split('d'))
		except Exception:
			await ctx.send('The format has to be in NdN!')
			return
		result = ', '.join(str(randint(1, limit)) for r in range(rolls))
		return int(result)

	@commands.command(name='dnd menu', description=f'A DND Menu',
					  aliases=['dndm', 'mdnd'],
					  usage='dndmenu is written together when using the command')
	async def dndmenu(self, ctx):
		menu_em = discord.Embed(title="Welcome to the DND Menu, traveller!",
								description="So what would you like adventurer?",
								color=discord.Color.red())
		menu_em.set_thumbnail(url=ctx.message.author.avatar_url)
		menu_em.set_footer(text=f"Requested by {ctx.message.author.name} - Today at: " + (
							  time.strftime("%I:%M %p")),
							  icon_url=self.azami.user.avatar_url)

		menumessage = "So choose from the following: \n" \
		"1) a!roll - Simple Roll Command\n" \
		"2) a!modroll - Simple Roll with modifier\n" \
		"3) a!initiative - Rolling for initiative\n" \
		"4) Quit - Exit Menu"

		menu_em.add_field(name="Menu Commands", value=menumessage)

		msg = await ctx.send(embed=menu_em)


		while True:
			await ctx.send(f"Waiting for you command, {ctx.message.author.name}", delete_after=3)
			msg2 = await ctx.send("Please enter a number 1 - 4")
			player = await self.azami.wait_for('message', timeout=120.00)
			if player.content == "4":
				await msg.delete()
				await msg2.delete()
				await ctx.send("See you next time!")
				return
			elif player.content == "1":
				await msg.delete()
				await msg2.delete()
				await ctx.send("Please enter NdN format, eg. 1d20")
				dice = await self.azami.wait_for('message')
				await self.roll(ctx, dice.content)
				break
			elif player.content == "2":
				await msg.delete()
				await msg2.delete()
				await ctx.send("Please enter NdNdN format, eg. 1d20d2")
				dice = await self.azami.wait_for('message')
				dice = dice.content
				try:
					rolls, limit, mod = map(int, dice.split('d'))
				except Exception:
					await ctx.send('The format has to be in NdNdN!')
					return
				dice = str(rolls) + "d" + str(limit)
				await self.roll(ctx, dice, mod)
				break
			elif player.content == "3": # Add more try and except catches
				await msg.delete()
				await msg2.delete()
				await ctx.send("How many players are playing?")
				while True:
					try:
						player = await self.azami.wait_for('message')
						player = int(player.content)
						break
					except Exception:
						await ctx.send("Please enter a integer")
				order = []
				for i in range(0, player):
					msg = await ctx.send(f'Player {i + 1}')
					msg2  = await ctx.send("Enter your name!")
					player_name = await self.azami.wait_for('message')
					player_name = player_name.content
					dice = '1d20'
					result = await self.initiative(ctx, dice)
					line = f"{player_name},"+str(result)
					name, score = line.split(',')
					score = int(score)
					order.append((name, score))
					await msg.delete()
					await msg2.delete()
				order.sort(key=lambda x: x[1], reverse=True)

				for name, score in order:
					await ctx.send(f"{name}, {score}")
				break








def setup(azami):
	azami.add_cog(Dnd(azami))