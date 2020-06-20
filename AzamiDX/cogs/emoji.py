import discord
from discord.ext import commands
from AzamiDX.core.utils import edit

class Emoji(commands.Cog):

	def __init__(self, azami):
		self.azami = azami

	@commands.command(description="Enlarge an emoji!")
	async def emoji(self, ctx, emoji: discord.Emoji):
		em = discord.Embed(color=3553599)
		em.set_image(url=emoji.url)
		await edit(ctx, embed=em)

	@commands.command(description="List the emojis' icons and names on the server! (Mod Only)",
					  aliases=['el'])
	@commands.has_permissions(manage_emojis=True)
	async def emojilist(self, ctx):
		emoji_em1 = discord.Embed(title=f"{ctx.message.guild}'s emojis Page 1")
		emoji_em2 = discord.Embed(title=f"{ctx.message.guild}'s emojis Page 2")
		emoji_str = ''
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
		try:
			for i in range(0, 25):
				emoji_str = f"{emoji_list[i]} <- **{emoji_list[i+emoji_count]}**\n"
				emoji_em1.add_field(name=f"{i+1}", value=emoji_str)
			for i in range(25, 51):
				emoji_str = f"{emoji_list[i]} <- **{emoji_list[i+emoji_count]}**\n"
				emoji_em2.add_field(name=f"{i+1}", value=emoji_str)
		except:
			pass
		await ctx.send(embed=emoji_em1)
		await ctx.send(embed=emoji_em2)

def setup(azami):
	azami.add_cog(Emoji(azami))