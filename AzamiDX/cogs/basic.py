import discord
from discord.ext import commands
from AzamiDX.core.utils import edit
from AzamiDX.etc.basic.updateembed import mainembed

class Basic(commands.Cog):

	def __init__(self, azami):
		self.azami = azami

	@commands.command(description='Hi!')
	async def hello(self, ctx):
		await edit(ctx, content=f"Hello!, {ctx.author.mention}")

	@commands.command(description='Get the latency of the bot')
	async def ping(self, ctx):
		await edit(ctx, content=f'Pong! :ping_pong: {round(self.azami.latency * 1000)}ms.')

	@commands.command(description="Gets your Guild's invite link")
	async def invite(self, ctx):
		server = ctx.message.guild
		try:
			invite = await server.invites()
			invite = invite[0]
			await edit(ctx, content=f"This guild's invite link: {invite}")
		except:
			invite = await ctx.channel.create_invite(reason="A server invite "\
						   "was created due to no existing server invite")
			await edit(ctx, content=f"This guild's invite link: {invite}")

	@commands.command(description="Gets Azami's support invite link",
					  aliases=['sserv'])
	async def supportserver(self, ctx):
		await edit(ctx, content="The support server invite: https://discord.gg/rRb23dt")

	@commands.command(description="My update logs!",
					  aliases=['ulogs'])
	async def updatelogs(self, ctx): # Logs
		await mainembed(self.azami, ctx)
		
	@invite.error
	async def invite_error(self, ctx, error):
		if isinstance(error, commands.CommandInvokeError):
			await ctx.send("Please assign 'create_invite' permissions to this bot")

def setup(azami):
	azami.add_cog(Basic(azami))