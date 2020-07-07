import aiohttp, discord, json, os, psycopg2, random
from discord.ext import commands
from discord.abc import Messageable
from asyncio import sleep
	

async def edit(ctx, content=None, embed=None, ttl=None):
	perms = ctx.channel.permissions_for(ctx.me).embed_links
	ttl = None if ctx.message.content.endswith(' stay') else ttl
	try:
		if ttl and perms:
			await ctx.send(content=content, embed=embed)
			await sleep(ttl)
			try:
				await ctx.message.delete()
			except:
				log.error(f'Failed to delete Message in {ctx.guild.name}, #{ctx.channel.name}')
				pass
		elif ttl is None and perms:
			await ctx.send(content=content, embed=embed)
		elif embed is None:
			await ctx.send(content=content, embed=embed)
		elif embed and not perms:
			await ctx.send(content='\N{HEAVY EXCLAMATION MARK SYMBOL} No Perms for Embeds', delete_after=5)
	except:
		if embed and not perms:
			await ctx.send(content='\N{HEAVY EXCLAMATION MARK SYMBOL} No Perms for Embeds', delete_after=5)
		else:
			await ctx.send(content=content, embed=embed, delete_after=ttl, file=None)

async def hastebin(content, session=None):
	session = aiohttp.ClientSession()
	async with session.post("https://hastebin.com/documents", data=content.encode('utf-8')) as resp:
		if resp.status == 200:
			result = await resp.json()
			await session.close()
			return "https://hastebin.com/" + result["key"]
		else:
			return f"Error with creating Hastebin, Status: {resp.status}"

async def pre_embed(titl:str, desc:str="", color=None, thumb_url:str="",
					image_url:str="", foot_txt:str="", foot_url:str="", ctx=None,
					num=0, fields: list=[], values: list=[]):
	if color == None:
		color = color_list()

	embed = discord.Embed(title=titl,
						  description=desc,
						  colour=color)

	
	embed.set_thumbnail(url=thumb_url)
	embed.set_image(url=image_url)
	embed.set_footer(text=foot_txt, icon_url=foot_url)

	for i in range(0, num):
		embed.add_field(name=fields[i], value=values[i])
	
	return embed

def color_list():
	colorList = [discord.Color.red(), discord.Color.green(), discord.Color.blue(),
				 discord.Color.orange(), discord.Color.purple(), discord.Color.gold(),
				 discord.Color.blurple(), discord.Color.greyple(), discord.Color.teal(),
				 discord.Color.dark_red(), discord.Color.dark_green(),
				 discord.Color.light_grey(), discord.Color.dark_gold()]
	colorList = random.choice(colorList)
	return colorList

try:
	db = psycopg2.connect(
	host="ec2-54-75-248-49.eu-west-1.compute.amazonaws.com",
	database="defh9ng1qcsr3r",
	user="yaffdhqkqalpvx",
	password="4bd878bee114c6476d9775135dfb8a28f324a3ac17f4996053df95072d7fcc38")
	mycursor = db.cursor()
except:
	db = ""
	mycursor = ""

async def get_prefix(azami, msg):
	try:
		mycursor.execute(f'SELECT command_prefix FROM prefix WHERE guild_id = {msg.guild.id}')
		custom_prefix = mycursor.fetchone()
		custom_prefix = custom_prefix[0]
	except:
		custom_prefix = "ab!"
	return commands.when_mentioned_or(custom_prefix)(azami, msg)





