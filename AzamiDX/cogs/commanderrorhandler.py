import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound, CheckFailure, NoPrivateMessage, MissingRequiredArgument
from AzamiDX.core.utils import edit

class CommandErrorHandler(commands.Cog):
	
	def __init__(self, azami):
		self.azami = azami

	@commands.Cog.listener()
	async def on_command_error(self, ctx, error):
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