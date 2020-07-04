import discord, aiohttp, time
from discord.ext import commands
from random import choice
from AzamiDX.core.utils import hastebin, color_list, edit, get_prefix
color_list = color_list()

class Server(commands.Cog):

	def __init__(self, azami):
		self.azami = azami

	@commands.command(description='This will display info about the server', aliases=["si"])
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
		em = discord.Embed(description= f"For the server: {server.name}",
						   color=color_list)
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
		em.set_author(name='Server Info', icon_url=self.azami.user.avatar_url)
		em.set_footer(text='Server ID: %s' % server.id)
		await edit(ctx, embed=em)

		

	@commands.command(description='This will display info about user or another user', aliases=["ui"])
	async def userinfo(self, ctx, *, name=""):
		if name:
			user = user = ctx.message.mentions[0]
		else:
			user = ctx.message.author

		if isinstance(user, discord.Member):
			role = user.top_role.name
			if role == "@everyone":
				role = 'N/A'

		em = discord.Embed(description= f"Information on: {user}",
						   color=color_list)
		em.add_field(name='User ID', value=user.id, inline=True)
		if isinstance(user, discord.Member):
			voice_state = None if not user.voice else user.voice.channel
			em.add_field(name='Nickname', value=user.nick, inline=True)
			em.add_field(name='Status', value=user.status, inline=True)
			em.add_field(name='In Voice', value=voice_state, inline=True)
			em.add_field(name='Activity', value=user.activity, inline=True)
			em.add_field(name='Highest Role', value=role, inline=True)
		em.add_field(name='Account Created', value=user.created_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
		if isinstance(user, discord.Member):
			em.add_field(name='Join Date', value=user.joined_at.__format__('%A, %d. %B %Y @ %H:%M:%S'))
		em.set_thumbnail(url=user.avatar_url)
		em.set_author(name=user, icon_url=self.azami.user.avatar_url)
		em.set_footer(text=f"Requested by {ctx.message.author.name} - Today at: " + (
							  time.strftime("%I:%M %p")))
		await edit(ctx, embed=em)

	@commands.command(description='This will display info about Azami!', aliases=["bi"])
	async def botinfo(self, ctx):
		command_prefix = await get_prefix(self.azami, ctx)
		command_prefix = command_prefix[2]
		guild_url = "https://discord.gg/rRb23dt"
		em = discord.Embed(title=self.azami.user.name,
						   description="My name is Azami, please to meet you! I hope we can get along!",
						   color=discord.Color.gold())
		em.add_field(name="Azami's ID", value=self.azami.user.id, inline=True)
		em.add_field(name='Owner of Azami', value="El Clear#9765", inline=True)
		em.add_field(name="Azami's Guild", value=f"[Gusty Garden]({guild_url})", inline=True)
		em.add_field(name="Azami's Default Prefix", value=self.azami.og_command_prefix, inline=True)
		em.add_field(name="Azami's Guild Prefix", value=command_prefix, inline=True)
		em.add_field(name="Azami's Help Command", value=f"{command_prefix}help", inline=True)
		em.set_thumbnail(url=self.azami.user.avatar_url)
		em.set_footer(text=f"Requested by {ctx.message.author.name} - Today at: " + (
							  time.strftime("%I:%M %p")))
		await ctx.send(embed=em)



def setup(azami):
	azami.add_cog(Server(azami))