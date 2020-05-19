import discord
from discord.ext import commands

class Mod(commands.Cog):

	def __init__(self, azami):
		self.azami = azami

	@commands.command()
	@commands.has_permissions(kick_members = True)
	async def kick(self, ctx, member: discord.Member, *, reason=None):
		await member.kick(reason=reason)
		await ctx.send(f"You have kicked, {member.mention}")

	@commands.command(ban_members = True)
	@commands.has_permissions(ban_members = True)
	async def ban(self, ctx, member: discord.Member, *, reason=None):
		await member.ban(reason=reason)
		await ctx.send(f"You have banned, {member.mention}")

	@commands.command(ban_members = True)
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


def setup(azami):
	azami.add_cog(Mod(azami))