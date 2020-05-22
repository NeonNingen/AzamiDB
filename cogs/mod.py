import discord
from discord.ext import commands
from discord.ext.commands import MissingRequiredArgument

class Mod(commands.Cog):

	def __init__(self, azami):
		self.azami = azami

	@commands.command(description="Watch your butts!")
	@commands.has_permissions(kick_members = True)
	async def kick(self, ctx, member: discord.Member, *, reason=None):
		await member.kick(reason=reason)
		await ctx.send(f"You have kicked, {member.mention}")

	@commands.command(description="I smite thee with thy hammer")
	@commands.has_permissions(ban_members = True)
	async def ban(self, ctx, member: discord.Member, *, reason=None):
		await member.ban(reason=reason)
		await ctx.send(f"You have banned, {member.mention}")

	@commands.command(description="You're can join back after a day")
	@commands.has_permissions(ban_members = True)
	async def softban(self, ctx, user: discord.User, *, reason=None):
		await ctx.guild.ban(user)
		await ctx.guild.unban(user)
		await ctx.send(f"I have softbanned {user}")

	@commands.command(description="I relinquish thy ban")
	@commands.has_permissions(ban_members = True)
	async def unban(self, ctx, *, member):
		banned_users = await ctx.guild.bans()
		member_name, member_discriminator = member.split('#')

		for ban_entry in banned_users:
			user = ban_entry.user

			if(user.name, user.discriminator) == (member_name, member_discriminator):
				await ctx.guild.unban(user)
				await ctx.send(f'You have unbanned, {user.mention}')
				return

	@commands.command(description="Watch me purge away!")
	@commands.has_permissions(manage_messages = True)
	async def clear(self, ctx, amount: int = 5):
		await ctx.channel.purge(limit = amount + 1)

	@kick.error
	async def kick_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send("You cannot use this command")
		elif isinstance(error, MissingRequiredArgument):
			await ctx.send("Requires an argument")
		

	@ban.error
	async def ban_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send("You cannot use this command")
		elif isinstance(error, MissingRequiredArgument):
			await ctx.send("Requires an argument")

	@unban.error
	async def unban_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send("You cannot use this command")
		elif isinstance(error, MissingRequiredArgument):
			await ctx.send("Requires an argument")
	
	@clear.error
	async def clear_error(self, ctx, error):
		if isinstance(error, commands.MissingPermissions):
			await ctx.send("You cannot use this command")
		elif isinstance(error, MissingRequiredArgument):
			await ctx.send("Requires an argument")
	
def setup(azami):
	azami.add_cog(Mod(azami))