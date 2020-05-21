import discord, random
from discord.ext import commands

color_list = [discord.Color.red(), discord.Color.green(), discord.Color.blue(),
			  discord.Color.orange(), discord.Color.purple(), discord.Color.gold(),
			  discord.Color.blurple(), discord.Color.greyple(), discord.Color.teal(),
			  discord.Color.dark_red(), discord.Color.dark_green(),
			  discord.Color.light_grey(), discord.Color.dark_gold()]

def chunks(self, l, n):
	for i in range(0, len(l), n):
		yield l[i:i + n]

class Help(commands.Cog):

	def __init__(self, azami):
		self.azami = azami

	@commands.command()
	def help(self, ctx):
		cmds_ = []
		cogs = ctx.bot.cogs
		for i in cogs:
			cmd_ = ctx.bot.get_cog(i).get_commands()
			cmd_ = [x for x in cmd_ if not x.hidden]
			for x in list(chunks(list(cmd_), 6)):
				embed = discord.Embed(color=discord.Color.blurple()) 
				embed.set_author(name=f"{i} Commands ({len(cmd_)})")
				embed.description = ctx.bot.cogs[i].__doc__
				for y in x:
					embed.add_field(name=y.signature, value=y.help, inline=False)
					cmds_.append(embed)

			for n, a in enumerate(cmds_):
				a.set_footer(
					text=f'Page {n+1} of {len(cmds_)} | Type "{ctx.prefix}help <command>" for more information')
		return cmds_

	@help.error
	async def help_error(self, ctx, error):
		if isinstance(error, commands.CommandError):
			await ctx.send("Well there is a issue with this command...")
		return error



	



def setup(azami):
	azami.add_cog(Help(azami))