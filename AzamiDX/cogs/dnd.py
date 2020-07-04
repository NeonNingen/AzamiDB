import discord, time, aiohttp, json
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument
from random import randint
from asyncio import sleep, TimeoutError
from AzamiDX.etc.img import display
from AzamiDX.etc.dnd.dndetc import return_results
from AzamiDX.etc.dnd.searchjson import startEquipment, levelling, spellfind, classfind
from AzamiDX.core.utils import hastebin, edit

class Dnd(commands.Cog):

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

		if limit <= 0:
			await ctx.send("Please roll a dice higher than 0")
			return

		if rolls > 10:
			await ctx.send("Cannot roll more than 10 dices")
			return

		roll_em = discord.Embed(title=f"Rolling {rolls} dice(s)",
								description=f"Hope you get a natural {limit}!",
								color=discord.Color.teal())
		roll_em.set_thumbnail(url=ctx.message.author.avatar_url)

		limits = {4: display.rollimg(1),
				  6: display.rollimg(2),
				  8: display.rollimg(3),
				  10: display.rollimg(4),
				  100: display.rollimg(5),
				  12: display.rollimg(6),
				  20: display.rollimg(7)}

		try:
			url = limits[limit]
		except KeyError:
			url = display.rollimg(8)

		roll_em.set_image(url=url)
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
					  usage='This will decide who gets to attack first',
					  aliases=['init'])
	async def initiative(self, ctx):
		await ctx.send("How many players are playing?")
		while True:
			def check(m):
				return m.author == ctx.author and m.channel == ctx.channel
			try:
				player = await self.azami.wait_for('message', check=check, timeout=3)
				playercont = int(player.content)
				await player.delete()
				order = []
				while True:
					for i in range(0, playercont):
						msg = await ctx.send(f'Player {i + 1}')
						msg2 = await ctx.send("Enter your name!")
						player_name = await self.azami.wait_for('message')
						player_namecont = player_name.content
						msg3 = await ctx.send("Enter your dex modifier")
						mod = await self.azami.wait_for('message', check=check)
						modcont = int(mod.content)
						result = return_results(0, -1,modcont)
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
				break
			except ValueError:
				await ctx.send("Please enter a integer")
			except TimeoutError:
				await ctx.send("Time out")
				break


	@commands.command(description="Search from spells across all of dnd 5e",
					  aliases=['ss'])
	async def spellsearch(self, ctx, *, content):
		spell_em = spellfind(self.azami.driver, content, ctx, self.azami)
		await ctx.send(embed=spell_em)

	@commands.command(description="Search from classes across all of dnd 5e.",
					  aliases=['cs'])
	async def classessearch(self, ctx, *, content):
		class_em = await classfind(self.azami.driver, content, ctx, self.azami, 0)
		await ctx.send(embed=class_em)

	@commands.command(description="Search from classes across all of dnd 5e. Just Simpler. Using http links!",
					  aliases=['hcs'])
	async def httpclassessearch(self, ctx, *, content):
		class_em = await classfind(self.azami.driver, content, ctx, self.azami, 1)
		await ctx.send(embed=class_em)

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