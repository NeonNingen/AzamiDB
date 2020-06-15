import discord, json
from discord.ext import commands
from selenium import webdriver
from AzamiDX.core.webdriver import get_driver
from AzamiDX.etc.waifu.searchhtml import newwaifufind

class Waifu(commands.Cog):

	def __init__(self, azami):
		self.azami = azami
		try:
			self.driver = get_driver()
		except:
			self.driver = webdriver.Chrome('./chromedriver')
		self.driver.minimize_window()

	@commands.command(description="Find a waifu!",
					  usage="Just do a!ws {waifu_name}",
					  aliases=['ws'])
	async def waifusearch(self, ctx, *, content):
		waifu_em = await newwaifufind(self.driver, content, ctx, self.azami)
		await waifu_em

def setup(azami):
	azami.add_cog(Waifu(azami))