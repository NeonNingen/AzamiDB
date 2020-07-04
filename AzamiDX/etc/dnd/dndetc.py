import discord
from AzamiDX.etc.img.display import diceimg
from random import randint

def return_results(limit, rolls, mod, i=0):

	if rolls == -1:
		dice = '1d20'
		rolls, limit = map(int, dice.split('d'))
		result = ', '.join(str(randint(1, limit)) for r in range(rolls))
		result = int(result)
		result += mod
		return result

	if rolls == 1:
		result = ', '.join(str(randint(1, limit)) for r in range(rolls))
		result = int(result)

		if mod > 0: result += mod

		result_em = discord.Embed(title=f"Here's your result!",
							  	  description=f"You got: {result}!",
							  	  color=discord.Color.gold())

		if result > 20:
			return result_em
		else:
			dicepic = diceimg(result)
			result_em.set_image(url=dicepic)
			return result_em

	else:
		multi_em = discord.Embed(title=f"Rolled so far {i+1}",
								 color=discord.Color.gold())
		limit = randint(1, limit)

		if mod > 0: limit += mod

		if limit > 20:
			return multi_em.add_field(name=f"Roll {i + 1}", value=f"This your value: {limit}")
		else:
			dicepic = diceimg(limit)
			multi_em.add_field(name=f"Roll {i + 1}", value=f"This your value: {limit}")
			multi_em.set_image(url=dicepic)
			return multi_em
	