import discord, random
from discord.ext import commands

color_list = [discord.Color.red(), discord.Color.green(), discord.Color.blue(),
			  discord.Color.orange(), discord.Color.purple(), discord.Color.gold(),
			  discord.Color.blurple(), discord.Color.greyple(), discord.Color.teal(),
			  discord.Color.dark_red(), discord.Color.dark_green(),
			  discord.Color.light_blue(), discord.Color.dark_gold()]

class Help(commands.Cog):

	def __init__(self, azami):
		self.azami = azami

	

	@commands.command(name="help", description="The help command!",usage="cog")
	async def help(self, ctx, cog="all"):
		help_embed = discord.Embed(title="Help",
								   color=color_list)
		help_embed.set_thumbnail(url=self.azami.user.avatar_url)
		help_embed.set_footer(text=f"Requested by {ctx.author.mention}",
							  icon_url=self.azami.user.avatar_url)

		cogs = [c for c in self.azami.cogs.keys()]

		if cog == 'all':
			for cog in cogs:
				cog_commands = self.azami.get_cog(cog).get_commands()
				commands_list = ''
				for comm in cog_commands:
					commands_list += f'**{comm.name}** - *{comm.description}*\n'

				help_embed.add_field(name=cog, value=commands_list, inline=False
									).add_field(name='\u200b', value='\u200b', 
												inline=False)
			pass
		else:
			lower_cogs = [c.lower() for c in cogs]

			if cog.lower() in lower_cogs:
				commands_list = self.azami.get_cog(cogs[lower_cogs.index(
															  cog.lower())]
															  ).get_commands()
				help_text = ''

				for commands in commands_list:
					help_text += f'```{command.name}```\n' \
						f'**{command.description}**\n\n'

					if len(commands.aliases) > 0:
						help_text += f'**Aliases: ** `{"`, `".join(command.aliases)}\n\n\n'
					else:
						help_text += '\n'

					help_text += f'Format: `@{self.azami.user.name}#{
											  self.azami.user.discriminator}' \
						f' {command.name} {
						command.usage if command.usage is not None else ""}`\n\n\n\n'

				help_embed.description = help_text
			else:
				await ctx.send(
					'Invalid cog specified.\nUse `help` command to list all cogs.')
				return

		await ctx.send(embed=help_embed)

		return



	



def setup(azami):
	azami.add_cog(Help(azami))