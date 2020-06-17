import discord
from discord.ext import commands
from AzamiDX.core.utils import edit
from AzamiDX.etc.help.helpembed import default_help_embed, cog_help_embed

class Help(commands.Cog):

	def __init__(self, azami):
		self.azami = azami
		azami.remove_command('help')

	@commands.command(description="The help command for guild!")
	async def help(self, ctx, cog: str = "default"):
		cog = cog.capitalize()
		cogs = [c for c in self.azami.cogs.keys()]
		while True:
			if cog == "Default":
				help_em = default_help_embed(self.azami, ctx)
				await edit(ctx, embed=help_em)
				break
			elif (cog in cogs) == True:
				help_em = cog_help_embed(self.azami, ctx, cog)
				await edit(ctx, embed=help_em)
				break
			else:
				await ctx.send("Please enter `a!help` or `a!help {cog}`")
				break

	@commands.command(description="The help command for DMs")
	async def dmhelp(self, ctx, cog: str = "default"):
		user = ctx.message.author
		cog = cog.capitalize()
		cogs = [c for c in self.azami.cogs.keys()]
		while True:
			if cog == "Default":
				help_em = default_help_embed(self.azami, ctx)
				await user.send(user, embed=help_em)
				break
			elif (cog in cogs) == True:
				help_em = cog_help_embed(self.azami, ctx, cog)
				await user.send(user, embed=help_em)
				break
			else:
				await ctx.send("Please enter `a!dmhelp` or `a!dmhelp {cog}`")
				break

def setup(azami):
	azami.add_cog(Help(azami))