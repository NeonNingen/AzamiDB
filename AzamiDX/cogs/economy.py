import discord
from discord.ext import commands

class Economy(commands.Cog):

	def __init__(self, azami):
		self.azami = azami

	@commands.command(description="Earn your money today!")
	@commands.cooldown(1, 900, commands.BucketType.user)
	async def daily(self, ctx):
		try:
			user_exists = self.azami.mycursor.execute(f"SELECT * FROM economy WHERE DiscordID = {ctx.author.id}")
			user_exists = self.azami.mycursor.fetchone()
			if user_exists:
				await ctx.send(f"Welcome back, {ctx.author.mention}! Here's some cash!:"\
			                	" 50 Rings")
				self.azami.mycursor.execute(f"UPDATE economy SET Balance = {user_exists[1] + 50} WHERE DiscordID = {ctx.author.id}")

			else:
				await ctx.send(f"Hello {ctx.author.mention}! I see this is your first time"\
				            	" getting money. So here 100 rings on the house!")
				Balance = 100
				self.azami.mycursor.execute(f"INSERT INTO economy (DiscordID, Balance) VALUES ({DiscordID}, {Balance})")
			self.azami.db.commit()
		except:
			await ctx.send("An Error Occurred, you cannot do this right now. Please try again later")

	@commands.command(description="How much balance do you have?",
					  aliases=['bal'])
	async def balance(self, ctx):
		try:
			user_exists = self.azami.mycursor.execute(f"SELECT * FROM economy WHERE DiscordID = {ctx.author.id}")
			user_exists = self.azami.mycursor.fetchone()
			if user_exists:
				balance = self.azami.mycursor.execute(f"SELECT * FROM economy WHERE DiscordID = {ctx.author.id}")
				balance = self.azami.mycursor.fetchone()
				balance = balance[1]
				await ctx.send(f"This is your balance: {balance} rings")
		except:
			await ctx.send("An Error Occurred, you cannot do this right now. Please try again later")
	
	@daily.error
	async def daily_error(self, ctx, error):
		if isinstance(error, commands.CommandOnCooldown):
			error = str(error).split()
			error = error[7]
			error = error.split("s")
			error = error[0]
			error = float(error)
			error /= 60
			error = round(error, 2)
			error = str(error).split(".")
			await ctx.send(f"You can use this command again in: **{error[0]}** min **{error[1]}** sec")

def setup(azami):
	azami.add_cog(Economy(azami))