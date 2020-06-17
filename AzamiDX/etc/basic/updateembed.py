import discord
from discord.ext import commands
from AzamiDX.etc.basic.version_list import version_num, version_desc
from AzamiDX.core.utils import color_list

color = color_list()

def updateembeds(azami, ctx, num): # Reinvent this before V2.2. More complex
	num -= 1
	em = discord.Embed()
	if num == 0:
		vtitle = version_num()[num]
		vdesc = version_desc()[num]
		em.title = vtitle
		em.description = vdesc
		em.color = color
		return em
	elif num == 1:
		vtitle = version_num()[num]
		vdesc = version_desc()[num]
		em.title = vtitle
		em.description = vdesc
		em.color = color
		return em
	elif num == 2:
		vtitle = version_num()[num]
		vdesc = version_desc()[num]
		em.title = vtitle
		em.description = vdesc
		em.color = color
		return em



async def mainembed(azami, ctx):
	member = ctx.message.author
	em = discord.Embed(title="Update logs: Main Menu",
					   color=color)
	em.description = "Please select the following options!\n" \
					 "Update 1: :one:\n"\
					 "Update 2: :two:\n"\
					 "Update 2.1: :new:\n"
	message = await ctx.send(embed=em)
	emoji1 = "1⃣"
	emoji2 = "2⃣"
	emoji3 = u"\U0001F195"
	uone = await message.add_reaction(emoji1)
	utwo = await message.add_reaction(emoji2)
	uthree = await message.add_reaction(emoji3)
	while True:
		reaction, user = await azami.wait_for('reaction_add', check=lambda r, u: member)
		if str(reaction) == str(emoji1) and user == member:
			for i in range(1, 4):
				tmps = 'emoji' + '%d' %i
				await message.clear_reaction(eval(tmps))
			num = 1
			em = updateembeds(azami, ctx, num)
			reaction_em = await message.edit(embed=em)
			return reaction_em
			break
		elif str(reaction) == str(emoji2) and user == member:
			for i in range(1, 4):
				tmps = 'emoji' + '%d' %i
				await message.clear_reaction(eval(tmps))
			num = 2
			em = updateembeds(azami, ctx, num)
			reaction_em = await message.edit(embed=em)
			return reaction_em
			break
		elif str(reaction) == str(emoji3) and user == member:
			for i in range(1, 4):
				tmps = 'emoji' + '%d' %i
				await message.clear_reaction(eval(tmps))
			num = 3
			em = updateembeds(azami, ctx, num)
			reaction_em = await message.edit(embed=em)
			return reaction_em
			break
		elif user == azami.user:
			pass 
		else:
			await ctx.send(f"Not your input: {user.name}")