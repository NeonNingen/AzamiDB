import discord, psycopg2
from discord.ext import commands

class Economy(commands.Cog):

	def __init__(self, azami):
		self.azami = azami
		self.db = psycopg2.connect(
			host="ec2-54-247-169-129.eu-west-1.compute.amazonaws.com",
			database="dfjlvlcd4d8rh4",
			user="pustxbwqtzxjbc",
			password="7d746eeaa1de5ec2f6b6d5a24dd4fb138b8a8a8f53f7d63836831aec78cf4c84")

		self.mycursor = self.db.cursor()

	@commands.command(description="Earn your money today!")
	async def daily(self, ctx):
		DiscordID = ctx.author.id
		user_exists = self.mycursor.execute(f"SELECT * FROM economy WHERE DiscordID = {ctx.author.id}")
		user_exists = self.mycursor.fetchone()
		if user_exists:
			await ctx.send(f"Welcome back, {ctx.author.mention}! Here's some cash!:"\
			                " 50 Rings")
			self.mycursor.execute(f"UPDATE economy SET Balance = {user_exists[1] + 50} WHERE DiscordID = {DiscordID}")

		else:
			await ctx.send(f"Hello {ctx.author.mention}! I see this is your first time"\
				            " getting money. So here 100 rings on the house!")
			Balance = 100
			self.mycursor.execute(f"INSERT INTO economy (DiscordID, Balance) VALUES ({DiscordID}, {Balance})")
		self.db.commit()

	@commands.command(description="How much balance do you have?")
	async def balance(self, ctx):
		user_exists = self.mycursor.execute(f"SELECT * FROM economy WHERE DiscordID = {ctx.author.id}")
		user_exists = self.mycursor.fetchone()
		if user_exists:
			balance = self.mycursor.execute(f"SELECT * FROM economy WHERE DiscordID = {ctx.author.id}")
			balance = self.mycursor.fetchone()
			balance = balance[1]
			await ctx.send(f"This is your balance: {balance} rings")

def setup(azami):
	azami.add_cog(Economy(azami))