import discord, time
from discord.ext import commands
from AzamiDX.core.utils import color_list

def default_help_embed(azami, ctx):
	cogs = [c for c in azami.cogs.keys()] # list of all cogs
	cogs.remove('Owner') # Remove cog(s) that are not used
	cog_num = len(cogs)
	url = "https://discord.gg/rRb23dt"
	desc = "The [] of each command contains an aliases for that command\n" \
			f"Use `{azami.og_command_prefix}help [cog] to get more help!` Example: `{azami.og_command_prefix}help Basic`\n" \
		 	f"For further help, join my [support server]({url})."

	em = discord.Embed(title="Help",
					   description=desc,
					   color=color_list())
	em.set_author(name=f"{azami.user.name}",
				  icon_url=azami.user.avatar_url)
	em.set_footer(text=f"Requested by {ctx.message.author.name} - Today at: " + (
				  time.strftime("%I:%M %p")),
				  icon_url=ctx.message.author.avatar_url)

	'''
	Lists insde a list, e.g. -> cog_name = [[], [], [], []]
	'''
	cog_name = [[] for i in range(cog_num)]
	cog_comm = [[] for i in range(cog_num)]
	cog_all_commands = []


	for i in range(0, cog_num): # Add seperate cogs for each lists inside a list
		for cog in cogs:
			cog_name[i].append(cog)

	for cog in cogs: # Count the amount of cogs
		cog_commands = azami.get_cog(cog).get_commands()
		cog_all_commands.append(cog_commands)

	command_num = len(cog_all_commands)
	commands_cog_list = ''

	for i in range(0, command_num):
		commands_list = azami.get_cog(cogs[i]).get_commands()
		for comm in commands_list:
			if len(comm.aliases) > 0:
				commands_cog_list = f"{comm.name}: {comm.aliases}"
				cog_comm[i].append(commands_cog_list)
			else:
				commands_cog_list = f"{comm.name}"
				cog_comm[i].append(commands_cog_list)
	

	cog_name_field = '' # fix commands output
	cog_cmd = ''

	for i in range(0, cog_num):
		for j in range(0, (command_num)):
			cog_cmd = ' \n'.join(cog_comm[i])
			cog_name_field = (f"{cog_name[0][i]} Cog")
		em.add_field(name=f"__{cog_name_field}__", value=f"```{cog_cmd}```")
	return em

def cog_help_embed(azami, ctx, cog):
	em = discord.Embed(title=f"{cog}",
					   color=color_list())
	cogs = [c for c in azami.cogs.keys()] 
	cogs.remove('Owner') 
	lower_cogs = [c.lower() for c in cogs]

	if cog.lower() in lower_cogs: # Find the cog from your cog search
		commands_list = azami.get_cog(cogs[lower_cogs.index(
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

			help_text += f'Format: `{azami.og_command_prefix}' \
						f'{command.name}`\n\n'

		em.description = help_text
	else:
		em.description = f'Invalid cog specified.\nUse `{command_prefix}help` command to list all cogs.'
		return em

	return em