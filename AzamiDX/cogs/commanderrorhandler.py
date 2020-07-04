import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound, CheckFailure, NoPrivateMessage, MissingRequiredArgument
from AzamiDX.core.utils import edit

class CommandErrorHandler(commands.Cog):
	
	def __init__(self, azami):
		self.azami = azami
		self.num = 0
	

	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
		channel = self.azami.get_channel(728911961131319328)
		self.num += 1
		error_em = discord.Embed(title=f"⚠️ Error {self.num} ",
								 description=f'```yaml\n{error}\n```',
								 color=discord.Color.red())
		error_em.add_field(name="Invoking Command", value=f'`{ctx.message.content}`')
		error_em.add_field(name="Author", value=f'`{ctx.message.author}`')
		await channel.send(embed=error_em)

		if isinstance(error, NoPrivateMessage):
			await edit(ctx, content='\N{HEAVY EXCLAMATION MARK SYMBOL} Only usable on Servers', ttl=5)
		elif isinstance(error, CheckFailure):
			await edit(ctx, content='\N{HEAVY EXCLAMATION MARK SYMBOL} No Permissions to use this command', ttl=5)
		elif isinstance(error, MissingRequiredArgument):
			await edit(ctx, content='\N{HEAVY EXCLAMATION MARK SYMBOL} Missing Argument', ttl=5)
		elif isinstance(error, CommandNotFound):
			await edit(ctx, content='Invalid command, did you type that right?', ttl=10)

def setup(azami):
	azami.add_cog(CommandErrorHandler(azami))