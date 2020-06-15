import aiohttp, discord, json, logging, os, psycopg2, random
from discord.ext import commands
from discord.abc import Messageable
from asyncio import sleep

log = logging.getLogger('LOG')
	

async def edit(ctx, content=None, embed=None, ttl=None):
	perms = ctx.channel.permissions_for(ctx.me).embed_links
	ttl = None if ctx.message.content.endswith(' stay') else ttl
	try:
		if ttl and perms:
			await ctx.message.edit(content=content, embed=embed)
			await sleep(ttl)
			try:
				await ctx.message.delete()
			except:
				log.error(f'Failed to delete Message in {ctx.guild.name}, #{ctx.channel.name}')
				pass
		elif ttl is None and perms:
			await ctx.message.send(content=content, embed=embed)
		elif embed is None:
			await ctx.message.edit(content=content, embed=embed)
		elif embed and not perms:
			await ctx.message.edit(content='\N{HEAVY EXCLAMATION MARK SYMBOL} No Perms for Embeds', delete_after=5)
	except:
		if embed and not perms:
			await ctx.message.edit(content='\N{HEAVY EXCLAMATION MARK SYMBOL} No Perms for Embeds', delete_after=5)
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

async def pre_embed(titl:str, desc:str="", color=None, thumb_url:str="", image_url:str="", text_em:str="", foot_url:str="", ctx=None):
	if color == None:
		color = color_list()

	embed = discord.Embed(title=titl,
						  description=desc,
						  colour=color)

	
	embed.set_thumbnail(url=thumb_url)
	embed.set_image(url=image_url)
	embed.set_footer(text=text_em, icon_url=foot_url)
	
	return embed

def str_cmd(s: str):
	return s.encode("ascii", "replace").decode("ascii")

def get_channel_and_guild_name(channel: Messageable):
	return ('DM' if isinstance(channel, discord.DMChannel) else str_cmd(channel.guild.name)), str_cmd(str(channel))

def error_on_message(m: discord.Message, error_message: str):
	# Log an error caused by a message
	guild_name, channel_name = get_channel_and_guild_name(m.channel)
	print(f"{m} has {error_message} -> Server Name: {guild_name}, channel_name: {channel_name}")

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
	host="ec2-54-247-169-129.eu-west-1.compute.amazonaws.com",
	database="dfjlvlcd4d8rh4",
	user="pustxbwqtzxjbc",
	password="7d746eeaa1de5ec2f6b6d5a24dd4fb138b8a8a8f53f7d63836831aec78cf4c84")
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





