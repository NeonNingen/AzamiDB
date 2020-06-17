import discord, time, aiohttp, json
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument
from random import randint
from asyncio import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from AzamiDX.etc.dnd.dndetc import return_results, hiddenrolls
from AzamiDX.etc.dnd.searchjson import startEquipment, levelling, spellfind, simpleclassfind, classfind
from AzamiDX.core.utils import color_list, hastebin, edit



class Dnd(commands.Cog): # Work on Embed Rolls also modifier addon

	def __init__(self, azami):
		self.azami = azami

	@commands.command(description=f'The format must be NdN',
					  usage='To roll any dice, any amount of times')
	async def roll(self, ctx, dice: str, mod=0):
		try:
			rolls, limit = map(int, dice.split('d'))
		except Exception:
			await edit(ctx, content='The format has to be in NdN!', ttl=5)
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
	async def initiative(self, ctx):
		await ctx.send("How many players are playing?")
		while True:
			def check(m):
				return m.author == ctx.author and m.channel == ctx.channel
			try:
				player = await self.azami.wait_for('message', check=check)
				playercont = int(player.content)
				await player.delete()
				break
			except Exception:
				await ctx.send("Please enter a integer")
		order = []
		for i in range(0, playercont):
			def check(m):
				return m.author == ctx.author and m.channel == ctx.channel
			msg = await ctx.send(f'Player {i + 1}')
			msg2 = await ctx.send("Enter your name!")
			player_name = await self.azami.wait_for('message', check=check)
			player_namecont = player_name.content
			msg3 = await ctx.send("Enter your dex modifier")
			while True:
				while True:
					def check(m):
						return m.author == ctx.author and m.channel == ctx.channel
					try:
						mod = await self.azami.wait_for('message', check=check)
						modcont = int(mod.content)
						break
					except Exception:
						await ctx.send("Please enter an integer")
				result = hiddenrolls(modcont)
				line = f"{player_namecont},"+str(result)
				name, score = line.split(',')
				score = int(score)
				order.append((name, score))
				await mod.delete()
				await msg.delete()
				await msg2.delete()
				await msg3.delete()
				order.sort(key=lambda x: x[1], reverse=True)
				break
					
		hastebin_list = []
		for name, score in order:
			line = f"{name}, {score}"
			await ctx.send(line)
			hastebin_list.append(line)
		_all = '\n'.join(hastebin_list)
		url = await hastebin(str(_all), None)
		hastebin_of_players = f'[List of all players in order]({url})'
		em = discord.Embed(name="Link for the player order!", 
						   description= hastebin_of_players,
						   color= discord.Color.blurple())
		await edit(ctx, embed=em)

	

	@commands.command(description="Search from spells across all of dnd 5e",
					  aliases=['ss'])
	async def spellsearch(self, ctx, *, content):
		spell_em = spellfind(self.azami.driver, content, ctx, self.azami)
		await ctx.send(embed=spell_em)
	
	

	@commands.command(description="Search from classes across all of dnd 5e.",
					  aliases=['cs'])
	async def classessearch(self, ctx, *, content):
		class_em = classfind(self.azami.driver, content, ctx, self.azami)
		await ctx.send(embed=class_em)

	@commands.command(description="Search from classes across all of dnd 5e. Just Simpler. Using http links!",
					  aliases=['hcs'])
	async def httpclassessearch(self, ctx, *, content):
		class_em = await simpleclassfind(self.azami.driver, content, ctx, self.azami)
		await ctx.send(embed=class_em)

	@commands.command(description=f'A DND Menu',
					  aliases=['dndm'])
	async def dndmenu(self, ctx, num=0):
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
		"4) a!spellsearch - Search for any spell in DND 5e\n" \
		"5) a!classessearch - Search for any class in DND 5e\n" \
		"6) a!htmlclasssearch - A cleaner way to search for classes in 5e\n" \
		"7) Quit - Exit Menu"

		menu_em.add_field(name="Menu Commands", value=menumessage)

		if num != 0:
			def check(m):
				return m.author == ctx.author and m.channel == ctx.channel
			if num == 1:
				await ctx.send("Please enter NdN format, eg. 1d20")
				dice = await self.azami.wait_for('message', check=check)
				await self.roll(ctx, dice.content)
				return
			elif num == 2:
				await ctx.send("Please enter NdNdN format, eg. 1d20d2")
				dice = await self.azami.wait_for('message', check=check)
				dice = dice.content
				try:
					rolls, limit, mod = map(int, dice.split('d'))
				except Exception:
					await ctx.send('The format has to be in NdNdN!')
					return
				dice = str(rolls) + "d" + str(limit)
				await self.roll(ctx, dice, mod)
				return
			elif num == 3:
				await self.initiative(ctx)
			elif num == 4:
				await ctx.send("Enter the spell you want to search for: ")
				player = await self.azami.wait_for('message', check=check)
				playercont = player.content
				await player.delete()
				spell_em = spellfind(self.azami.driver, playercont, ctx, self.azami)
				await ctx.send(embed=spell_em)
				return
			elif num == 5:
				await ctx.send("Enter the class you want to search for: ")#
				player = await self.azami.wait_for('message', check=check)
				playercont = player.content
				await player.delete()
				class_em = classfind(self.azami.driver, playercont, ctx, self.azami)
				await ctx.send(embed=class_em)
				return
			elif num == 6:
				await ctx.send("Enter the class you want to search for: ")
				player = await self.azami.wait_for('message', check=check)
				playercont = player.content
				await player.delete()
				spell_em = await simpleclassfind(self.azami.driver, playercont, ctx, self.azami)
				await ctx.send(embed=spell_em)
				return
			elif num == 7:
				await ctx.send("See you next time!")
				return

		msg = await ctx.send(embed=menu_em)

		while True:
			def check(m):
				return m.author == ctx.author and m.channel == ctx.channel
			await ctx.send(f"Waiting for you command, {ctx.message.author.name}", delete_after=3)
			msg2 = await ctx.send("Please enter a number 1 - 7")
			player = await self.azami.wait_for('message', timeout=120.00, check=check)
			if player.content == "7":
				await msg.delete()
				await msg2.delete()
				await ctx.send("See you next time!")
				return
			elif player.content == "1":
				def check(m):
					return m.author == ctx.author and m.channel == ctx.channel
				await msg.delete()
				await msg2.delete()
				await ctx.send("Please enter NdN format, eg. 1d20")
				dice = await self.azami.wait_for('message', check=check)
				await self.roll(ctx, dice.content)
				break
			elif player.content == "2":
				def check(m):
					return m.author == ctx.author and m.channel == ctx.channel
				await msg.delete()
				await msg2.delete()
				await ctx.send("Please enter NdNdN format, eg. 1d20d2")
				dice = await self.azami.wait_for('message', check=check)
				dice = dice.content
				try:
					rolls, limit, mod = map(int, dice.split('d'))
				except Exception:
					await ctx.send('The format has to be in NdNdN!')
					return
				dice = str(rolls) + "d" + str(limit)
				await self.roll(ctx, dice, mod)
				break
			elif player.content == "3":
				await msg.delete()
				await msg2.delete()
				await self.initiative(ctx)
				break
			elif player.content == "4":
				def check(m):
					return m.author == ctx.author and m.channel == ctx.channel
				await msg.delete()
				await msg2.delete()
				await ctx.send("Enter the spell you want to search for: ")
				player = await self.azami.wait_for('message', check=check)
				playercont = player.content
				await player.delete()
				spell_em = spellfind(self.azami.driver, playercont, ctx, self.azami)
				await ctx.send(embed=spell_em)
				break
			elif player.content == "5":
				def check(m):
					return m.author == ctx.author and m.channel == ctx.channel
				await msg.delete()
				await msg2.delete()
				await ctx.send("Enter the class you want to search for: ")
				player = await self.azami.wait_for('message', check=check)
				playercont = player.content
				await player.delete()
				class_em = classfind(self.azami.driver, playercont, ctx, self.azami)
				await ctx.send(embed=class_em)
				break
			elif player.content == "6":
				def check(m):
					return m.author == ctx.author and m.channel == ctx.channel
				await msg.delete()
				await msg2.delete()
				await ctx.send("Enter the class you want to search for: ")
				player = await self.azami.wait_for('message', check=check)
				playercont = player.content
				await player.delete()
				spell_em = await simpleclassfind(self.azami.driver, playercont, ctx, self.azami)
				await ctx.send(embed=spell_em)
				break

	
	@spellsearch.error
	async def spellsearch_error(self, ctx, error):
		if isinstance(error, commands.CommandInvokeError):
			await ctx.send(f"Incorrect Spell given")

	@classessearch.error
	async def classessearch_error(self, ctx, error):
		if isinstance(error, commands.CommandInvokeError):
			await ctx.send(f"Incorrect Class given")

	@httpclassessearch.error
	async def httpclassessearch_error(self, ctx, error):
		if isinstance(error, commands.CommandInvokeError):
			await ctx.send(f"Incorrect Class given")


def setup(azami):
	azami.add_cog(Dnd(azami))