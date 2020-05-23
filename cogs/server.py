import discord, aiohttp
from discord.ext import commands
from random import choice

color_list = [discord.Color.red(), discord.Color.green(), discord.Color.blue()]

# In Azami 2.0: Use a import system for the colours like eg. from cogs.color import color_list

async def hastebin(content, session=None): # Move to cogs/utils/check in future
	if not session:
		session = aiohttp.ClientSession()
	async with session.post("https://hastebin.com/documents", data=content.encode('utf-8')) as resp:
		if resp.status == 200:
			result = await resp.json()
			await session.close()
			return "https://hastebin.com/" + result["key"]
		else:
			return f"Error with creating Hastebin, Status: {resp.status}" 
		

class Server(commands.Cog):

	def __init__(self, azami):
		self.azami = azami

	@commands.command(description="This will display info about the server", aliases=["si"])
	async def serverinfo(self, ctx):
		server = ctx.message.guild
		online = 0
		for i in server.members:
			if str(i.status) == 'online' or str(i.status) == 'idle' or str(i.status) == 'dnd':
				online += 1
		all_users = []
		for user in server.members:
			all_users.append(f'{user.name}')
		all_users.sort()
		_all = '\n'.join(all_users)
		channel_count = len([x for x in server.channels if type(x) == discord.channel.TextChannel])
		role_count = len(server.roles)
		emoji_count = len(server.emojis)
		em = discord.Embed(name="Server Info",
						   description= f"For the server: {server.name}",
						   color=choice(color_list))
		em.add_field(name='Name', value=server.name)
		em.add_field(name='Owner', value=server.owner, inline=False)
		em.add_field(name='Members', value=server.member_count)
		em.add_field(name='Currently Online', value=online)
		em.add_field(name='Text Channels', value=str(channel_count))
		em.add_field(name='Region', value=server.region)
		em.add_field(name='Verification Level', value=str(server.verification_level))
		em.add_field(name='Highest role', value=server.roles[role_count - 1])
		em.add_field(name='Number of roles', value=str(role_count))
		em.add_field(name='Number of emotes', value=str(emoji_count))
		url = await hastebin(str(_all), None)
		hastebin_of_users = f'[List of all {server.member_count} users in this server]({url})'
		em.add_field(name='Users', value=hastebin_of_users)
		em.add_field(name='Created At', value=server.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
		em.set_thumbnail(url=server.icon_url)
		em.set_author(name='Server Info', icon_url='https://i.imgur.com/RHagTDg.png')
		em.set_footer(text='Server ID: %s' % server.id)
		await ctx.send(embed=em)

		


		'''
		await ctx.send(f"This the amount of members online: {online}\n{_all}" \
			f"\nThis is the channel count: {channel_count}\nThis is the role count: {role_count}" \
			f"\nThis is the emoji count: {emoji_count}")
		'''






def setup(azami):
	azami.add_cog(Server(azami))