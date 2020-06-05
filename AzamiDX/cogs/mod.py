import discord
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument
from AzamiDX.core.utils import edit

class Mod(commands.Cog):

	def __init__(self, azami):
		self.azami = azami


	@commands.command(description='Watch your butts!',
					  usage='This command only works for moderators')
	@commands.has_permissions(kick_members = True)
	async def kick(self, ctx, member: discord.Member, *, reason=None):
		await member.kick(reason=reason)
		if reason != None:
			await edit(ctx, content=f"You have kicked, {member.mention} "\
									f"reason: {reason}")
		else:
			await edit(ctx, content=f"You have kicked, {member.mention}")

	@commands.command(description='I smite thee with thy hammer',
					  usage='This command only works for moderators')
	@commands.has_permissions(ban_members = True)
	async def ban(self, ctx, member: discord.Member, *, reason=None):
		await member.ban(reason=reason)
		if reason != None:
			await edit(ctx, content=f"You have banned, {member.mention} "\
									f"reason: {reason}")
		else:
			await edit(ctx, content=f"You have banned, {member.mention}")

	@commands.command(description='I relinquish thy ban',
					  usage='This command only works for moderators')
	@commands.has_permissions(ban_members = True)
	async def unban(self, ctx, *, member):
		banned_users = await ctx.guild.bans()
		member_name, member_discriminator = member.split('#')

		for ban_entry in banned_users:
			user = ban_entry.user

			if(user.name, user.discriminator) == (member_name, member_discriminator):
				await ctx.guild.unban(user)
				await edit(ctx, content=f'You have unbanned, {user.mention}')
				return

	@commands.command(description='Silence!',
					  usage='This command only works for moderators')
	@commands.has_permissions(manage_roles=True)
	async def mute(self, ctx, member: discord.Member, *, msg=None):
		role = discord.utils.get(member.guild.roles, name="Muted")
		if role in member.roles:
			await edit(ctx, content=f'{member.mention} is already muted')
		elif msg == None:
			await member.add_roles(role)
			await edit(ctx, content=f'{member.mention} was muted')
		else:
			await member.add_roles(role)
			await edit(ctx, content=f'{member.mention} was muted. Reason: {msg}')

	@commands.command(description='Go ahead, speak',
					  usage='This command only works for moderators')
	@commands.has_permissions(manage_roles=True)
	async def unmute(self, ctx, member: discord.Member):
		role = discord.utils.get(member.guild.roles, name="Muted")
		if role not in member.roles:
			await edit(ctx, content=f'{member.mention} is already unmuted')
		else:
			await member.remove_roles(role)
			await edit(ctx, content=f"{member.mention} is now unmuted")

	@commands.command(description='Watch me purge away!',
					  usage='This command only works for moderators')
	@commands.has_permissions(manage_messages=True)
	async def clear(self, ctx, amount: int = 5):
		await ctx.channel.purge(limit = amount + 1)

	@commands.command(description='Give a role!', aliases=["ar", "giverole", "gr"],
					  usage='This command only works for moderators')
	@commands.has_permissions(manage_roles=True)
	async def addrole(self, ctx, user: discord.Member, role: discord.Role):
		await user.add_roles(role)
		await edit(ctx, content=f"Hey {ctx.author.name}, {user.name} has been given a role called: {role.name}")

	@commands.command(description="I'll leach your role!", aliases=["rr"],
					  usage='This command only works for moderators')
	@commands.has_permissions(manage_roles= True)
	async def removerole(self, ctx, user: discord.Member, role: discord.Role):
		await user.remove_roles(role)
		await edit(ctx, content=f"Hey {ctx.author.name}, {user.name} has lost a role called: {role.name}")

	@commands.command(description="I'll add/remove this role", aliases=["sr"],
					  usage='This command only works for moderators')
	@commands.has_permissions(manage_roles = True)
	async def selfrole(self, ctx, choice, role: discord.Role):
		user = ctx.message.author
		if choice == "add":
			await user.add_roles(role)
			await edit(ctx, content=f"You now have acquired the role: {role.name}")
		elif choice == "remove":
			await user.remove_roles(role)
			await edit(ctx, content=f"You have thrown away the role: {role.name}")
		else:
			await edit(ctx, content="Error")

	''' Fix in future

	@commands.command(description="Setup the log channel and I'll do the rest",
					  usage='This command only works for moderators',
					  aliases=['lc'])
	@commands.has_permissions(manage_messages=True)
	async def log_channel(self, ctx, channel: discord.TextChannel):
		await edit(ctx, f"This channel's name is {channel.name}")

	'''

	@mute.error
	async def mute_error(self, ctx, error):
		if isinstance(error, commands.BadArgument):
			await ctx.send("Invalid Argument, please mention a user with {@user} ")

	@unmute.error
	async def unmute_error(self, ctx, error):
		if isinstance(error, commands.BadArgument):
			await ctx.send("Invalid Argument, Give me a muted user from this server ")


def setup(azami):
	azami.add_cog(Mod(azami))