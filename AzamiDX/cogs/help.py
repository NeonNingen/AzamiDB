import discord, time
from discord.ext import commands
from random import choice
from AzamiDX.core.utils import color_list, edit, get_prefix

color_list = color_list()

class Help(commands.Cog):

	def __init__(self, azami):
		self.azami = azami
		azami.remove_command('help')


	@commands.command(name="help", description="The help command!",usage="cog")
	async def help(self, ctx, cog="all"):
		command_prefix = "a!"
		help_embed = discord.Embed(title="Help",
								   description="Remember to use " + f"{command_prefix}" + "`{commandname}`",
								   color=color_list)
		help_embed.set_thumbnail(url=self.azami.user.avatar_url)
		help_embed.set_footer(text=f"Requested by {ctx.message.author.name} - Today at: " + (
							  time.strftime("%I:%M %p")),
							  icon_url=self.azami.user.avatar_url)

		cogs = [c for c in self.azami.cogs.keys()]
		cogs.remove('Waifu')
		cogs.remove('Owner')

		if cog == 'all':
			for cog in cogs:
				cog_commands = self.azami.get_cog(cog).get_commands()
				commands_list = ''
				for comm in cog_commands:
					commands_list += f'**{comm.name}** - *{comm.description}*\n'

				help_embed.add_field(name='\n' + cog, value=commands_list, inline=False)

			pass
			help_extra = "**Use " + f"{command_prefix}" + "help `{cog}` for more information on a cog**"
			help_embed.add_field(name="Need more help?", value=help_extra)
		else:
			lower_cogs = [c.lower() for c in cogs]

			if cog.lower() in lower_cogs:
				commands_list = self.azami.get_cog(cogs[lower_cogs.index(
															  cog.lower())]
															  ).get_commands()
				help_text = ''

				for command in commands_list:
					help_text += f'```{command.name}```\n' \
						f'**Description: {command.description}**\n' \
						f'{"**Usage: " + command.usage + "**" if command.usage is not None else ""}'

					if len(command.aliases) > 0:
						help_text += f'\n**Aliases: ** `{"`, `".join(command.aliases)}`\n'
					else:
						help_text += '\n'

					help_text += f'Format: `{command_prefix}' \
						f'{command.name}`\n\n'

				help_embed.description = help_text
			else:
				await edit(ctx,
					content=f'Invalid cog specified.\nUse `{command_prefix}help` command to list all cogs.')
				return

		await edit(ctx, embed=help_embed)

		return



def setup(azami):
	azami.add_cog(Help(azami))
