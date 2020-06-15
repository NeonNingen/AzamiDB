import discord, json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from AzamiDX.core.utils import color_list

def waifufind(driver, content, ctx, name):
	wait = WebDriverWait(driver, 5)
	driver.get(content)
	appears = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="waifu-core-information"]/div[1]/div[2]/div[2]/div/a'))).text
	desc = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="description"]'))).text
	image = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[2]/div[2]/div'))).get_attribute('style')[56:-3]
	popular = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="popularity-rank"]'))).text[13:18]
	
	tag = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div[1]/div/div[1]/div/div/div'))).text	
	place_of_og = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="origin"]'))).text
	age = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="age"]'))).text
	date_of_birth = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="birthday"]'))).text
	height = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="height"]'))).text
	weight = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="weight"]'))).text
	blood_type = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="blood-type"]'))).text
	bust = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="bust"]'))).text
	waist = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="waist"]'))).text
	hip = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="hip"]'))).text

	em = discord.Embed(title=f"{name}",
						   description=f"{desc}",
						   color=color_list())
	em.set_image(url=image)
	em.add_field(name="Popularity", value=popular)
	em.add_field(name="Appears in", value=appears)

	if tag:
		em.add_field(name="Tag", value=tag)

	if place_of_og:
		em.add_field(name="Place Of Origin", value=place_of_og)
	if age:
		em.add_field(name="Age", value=age)
	if date_of_birth:
		em.add_field(name="Date Of Birth", value=date_of_birth)
	if height:
		em.add_field(name="Height", value=height)
	if weight:
		em.add_field(name="Weight", value=weight)
	if blood_type:
		em.add_field(name="Blood Type", value=blood_type)
	if bust:
		em.add_field(name="Bust", value=bust)
	if waist:
		em.add_field(name="Waist", value=waist)
	if hip:
		em.add_field(name="Hip", value=hip)

	return em

async def newwaifufind(driver, content, ctx, azami):
	em = discord.Embed(title=f"{content.capitalize()} Search!",
					   color=color_list())
	try:
		em2 = discord.Embed(title=f"{content.capitalize()}",
					       color=color_list())
		bot_msg = await ctx.send("Please wait...")
		driver.get(f"https://mywaifulist.moe/browse")
		wait = WebDriverWait(driver, 5)
		inputElement = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div/div[1]/div[1]/input')))
		inputElement.send_keys(content)
		inputElement = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div/div[3]/button'))).click()
		waifus = []
		try:
			num = 0
			def check(m):
				return m.author == ctx.author and m.channel == ctx.channel
			for i in range(1, 26):
				waifu = wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="app"]/div/div/div[1]/div/div/div[4]/div[1]/table/tbody/tr[{i}]/td[1]/a')))
				series = wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="app"]/div/div/div[1]/div/div/div[4]/div[1]/table/tbody/tr[{i}]/td[2]/ul/li/a')))
				waifus.append(waifu.get_attribute('href'))
				em.add_field(name=f"Option {i}", value=waifu.text + "\n" + series.text)
				num += 1
		except:
			pass
		await bot_msg.delete()
		em.description = f"{num} options were found!"
		msg = await ctx.send(embed=em)
		bot_msg = await ctx.send(f"Pick an option from 1 to {num}! or q to quit")
			
		choose = await azami.wait_for('message', check=check)

		if choose.content == "q":
			em2.add_field(name="Goodbye", value="See you next time!")
			await bot_msg.delete()
			return msg.edit(embed=em2)
		else:
			try:
				choose = int(choose.content)
				waifu_name = wait.until(EC.presence_of_element_located((By.XPATH, f'//*[@id="app"]/div/div/div[1]/div/div/div[4]/div[1]/table/tbody/tr[{choose}]/td[1]/a')))
				waifu = waifus[choose - 1]
				em2 = waifufind(driver, waifu, ctx, waifu_name.text)
				await bot_msg.delete()
				return msg.edit(embed=em2)
			except:
				em2.add_field(name="Make sure to input a number", value="Invalid num!")
				await bot_msg.delete()
				return msg.edit(embed=em2)
				
	except:
		em.description("An Error Occurred")
		return ctx.send(embed=em)
		
			
		# waifu = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="app"]/div/div/div[1]/div/div/div[4]/div[1]/table/tbody/tr[1]/td[1]/a'))).get_attribute('href')
		# driver.get(waifu)