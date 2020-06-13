import discord
from discord.ext import commands
from AzamiDX.core.utils import edit

class Emoji(commands.Cog):

	def __init__(self, azami):
		self.azami = azami

	@commands.command(description="List the emojis' icons and names on the server!",
					  aliases=['el'])
	async def emojilist(self, ctx):
		server = ctx.message.guild
		emoji_count = len(server.emojis)
		await ctx.send(f"There is {emoji_count} emoji(s) on this server!")
		await ctx.send(f"The emojis are:")
		emoji_list = []
		for emoji_img in server.emojis:
			emoji_list.append(emoji_img)
		for emoji_img in server.emojis:
			emoji_img = str(emoji_img).split(':')
			emoji_img = emoji_img[1]
			emoji_list.append(emoji_img)
		for i in range(0, len(emoji_list)):
			await ctx.send(f"{emoji_list[i]} <- **{emoji_list[i+emoji_count]}**")

	@commands.command(description="List the emojis' names on the server!",
					  aliases=['eln'])
	async def emojilistname(self, ctx):
		server = ctx.message.guild
		emoji_count = len(server.emojis)
		await ctx.send(f"There is {emoji_count} emoji(s) on this server!")
		await ctx.send(f"The emojis are:")
		for emoji_name in server.emojis:
			emoji_name = str(emoji_name).split(':')
			emoji_name = emoji_name[1]
			await ctx.send(f"{emoji_name}")

	@commands.command(name='enlarge',
					  description="Enlarge an emoji!",
					  aliases=['emoji'])
	async def enlargeemoji(self, ctx, emoji: discord.Emoji):
		em = discord.Embed(color=3553599)
		em.set_image(url=emoji.url)
		await edit(ctx, embed=em)

def setup(azami):
	azami.add_cog(Emoji(azami))