import discord, sys
from discord.ext import commands
from random import randint
from asyncio import sleep
sys.path.insert(1, '../')
from diceimg import diceroll

def return_results(limit, rolls):
	result = ', '.join(str(randint(1, limit)) for r in range(rolls))
	result_em = discord.Embed(title=f"Here's your result!",
							  description=f"You got: {result}!",
							  color=discord.Color.gold())
	result = int(result)
	if result > 20:
		return result_em
	else:
		dicepic = diceroll(result)
		result_em.set_image(url=dicepic)
		return result_em

class Dnd(commands.Cog): # Work on Embed Rolls also modifier addon

	def __init__(self, azami):
		self.azami = azami

	@commands.command(description='To roll do `a!roll NdN`')
	async def roll(self, ctx, dice: str):
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
			await ctx.send(embed=roll_em)
			await sleep(3)
			result_em = return_results(limit, rolls)
			result_em.set_thumbnail(url=ctx.message.author.avatar_url)
			await ctx.send(embed=result_em)

		elif limit == 6:
			roll_em.set_image(url="https://bestanimations.com/Games/Dice/rolling-dice-gif-1.gif")
			roll_em.add_field(name=f"Currently rolling {rolls}d{limit}", value="\u200b")
			await ctx.send(embed=roll_em)
			await sleep(3)
			result_em = return_results(limit, rolls)
			result_em.set_thumbnail(url=ctx.message.author.avatar_url)
			await ctx.send(embed=result_em)

		elif limit == 8:
			roll_em.set_image(url="https://66.media.tumblr.com/457d10f08e468d1392ab7165ab330ba7/dc90dde4ae909e0f-2b/s400x600/a62e416692fcddf76e7623d560b89a8ad102a5c6.gifv")
			roll_em.add_field(name=f"Currently rolling {rolls}d{limit}", value="\u200b")
			await ctx.send(embed=roll_em)			
			await sleep(3)
			result_em = return_results(limit, rolls)
			result_em.set_thumbnail(url=ctx.message.author.avatar_url)
			await ctx.send(embed=result_em)

		elif limit == 10:
			roll_em.set_image(url="https://66.media.tumblr.com/3096dd055c2c00055e68e46695d18b09/23077a30d50cc0d0-93/s400x600/0936ec389211b11f159f79265b15a44370e8688a.gifv")
			roll_em.add_field(name=f"Currently rolling {rolls}d{limit}", value="\u200b")
			await ctx.send(embed=roll_em)
			await sleep(3)
			result_em = return_results(limit, rolls)
			result_em.set_thumbnail(url=ctx.message.author.avatar_url)
			await ctx.send(embed=result_em)

		elif limit == 100:
			roll_em.set_image(url="https://i.pinimg.com/originals/2f/d5/73/2fd573b2f3c6499ec3963b77475b43b2.png")
			roll_em.add_field(name=f"Currently rolling {rolls}d{limit}", value="\u200b")
			await ctx.send(embed=roll_em)
			await sleep(3)
			result_em = return_results(limit, rolls)
			result_em.set_thumbnail(url=ctx.message.author.avatar_url)
			await ctx.send(embed=result_em)

		elif limit == 12:
			roll_em.set_image(url="https://webstockreview.net/images/dice-clipart-d12-5.png")
			roll_em.add_field(name=f"Currently rolling {rolls}d{limit}", value="\u200b")
			await ctx.send(embed=roll_em)
			await sleep(3)
			result_em = return_results(limit, rolls)
			result_em.set_thumbnail(url=ctx.message.author.avatar_url)
			ctx.send(embed=result_em)

		elif limit == 20:
			roll_em.set_image(url="https://66.media.tumblr.com/1458225a6051e572f34b931011630d71/tumblr_ol1es3Lg4a1tevcm3o1_400.gifv")
			roll_em.add_field(name=f"Currently rolling {rolls}d{limit}", value="\u200b")
			await ctx.send(embed=roll_em)
			await sleep(3)
			result_em = return_results(limit, rolls)
			result_em.set_thumbnail(url=ctx.message.author.avatar_url)
			await ctx.send(embed=result_em)

		else:
			roll_em.set_image(url="https://cdn.shopify.com/s/files/1/1483/3510/products/Haunted_Dice_Ice_grande.gif")
			roll_em.add_field(name=f"Currently rolling {rolls}d{limit}", value="\u200b")
			await ctx.send(embed=roll_em)
			await sleep(3)
			result_em = return_results(limit, rolls)
			result_em.set_thumbnail(url=ctx.message.author.avatar_url)
			await ctx.send(embed=result_em)

		


def setup(azami):
	azami.add_cog(Dnd(azami))