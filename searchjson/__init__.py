import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait

def startEquipment(driver, body):
	y = json.loads(body)
	startEquipmentUrl = y['starting_equipment']['url']
	driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
	driver.get(f"https://www.dnd5eapi.co{startEquipmentUrl}")
	body2 = driver.find_element_by_xpath('/html/body/pre').text
	y2 = json.loads(body2)

	valueStartEquipmentDef = [y2['starting_equipment'][x]['item']['name'] + " " + str(y2['starting_equipment'][0]['quantity']) for x in range(len(y2['starting_equipment']))] 
	valueStartEquipmentDef = '\n'.join(p for p in valueStartEquipmentDef)
	valueStartEquipmentChoose = y2['choices_to_make']

	try:
		valueStartEquipmentChoiceA1 = ["a) " + y2['choice_1'][0]['from'][x]['item']['name'] + " or " + y2['choice_1'][1]['from'][x]['item']['name'] for x in range(len(y2['choice_1'][0]['from']))]
		valueStartEquipmentChoiceA2 = [y2['choice_1'][2]['from'][x]['item']['name'] for x in range(len(y2['choice_1'][2]['from']))]
		valueStartEquipmentChoiceA1 = ', '.join(p for p in valueStartEquipmentChoiceA1)
		valueStartEquipmentChoiceA2 = ', '.join(p for p in valueStartEquipmentChoiceA2)
		valueStartEquipmentChoiceA = valueStartEquipmentChoiceA1+" or "+valueStartEquipmentChoiceA2
	except:
		valueStartEquipmentChoiceA1 = ["a) " + y2['choice_1'][0]['from'][x]['item']['name'] for x in range(len(y2['choice_1'][0]['from']))]
		valueStartEquipmentChoiceA2 = [y2['choice_1'][1]['from'][x]['item']['name'] for x in range(len(y2['choice_1'][1]['from']))]
		valueStartEquipmentChoiceA1 = ', '.join(p for p in valueStartEquipmentChoiceA1)
		valueStartEquipmentChoiceA2 = ', '.join(p for p in valueStartEquipmentChoiceA2)
		valueStartEquipmentChoiceA = valueStartEquipmentChoiceA1+" or "+valueStartEquipmentChoiceA2

	try:
		valueStartEquipmentChoiceB = ["b) " + y2['choice_2'][0]['from'][x]['item']['name'] + " or " + y2['choice_2'][1]['from'][x]['item']['name'] for x in range(len(y2['choice_2'][0]['from']))]
		valueStartEquipmentChoiceB = ', '.join(p for p in valueStartEquipmentChoiceB)
	except:
		valueStartEquipmentChoiceB = ["b) " + y2['choice_2'][0]['from'][x]['item']['name'] for x in range(len(y2['choice_2'][0]['from']))]
		valueStartEquipmentChoiceB = ', '.join(p for p in valueStartEquipmentChoiceB)

	try:
		valueStartEquipmentChoiceC1 = ["c) " + y2['choice_3'][0]['from'][x]['item']['name'] for x in range(len(y2['choice_3'][0]['from']))]
		valueStartEquipmentChoiceC2 = [y2['choice_3'][1]['from'][x]['item']['name'] for x in range(len(y2['choice_3'][1]['from']))]
		valueStartEquipmentChoiceC1 = ', '.join(p for p in valueStartEquipmentChoiceC1)
		valueStartEquipmentChoiceC2 = ', '.join(p for p in valueStartEquipmentChoiceC2)#
		valueStartEquipmentChoiceC = valueStartEquipmentChoiceC1+" or "+valueStartEquipmentChoiceC2
	except:
		valueStartEquipmentChoiceC = "N/A"

	driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w') 
	return valueStartEquipmentDef, valueStartEquipmentChoose ,valueStartEquipmentChoiceA, valueStartEquipmentChoiceB, valueStartEquipmentChoiceC

def levelling(driver, body):
	y = json.loads(body)
	levellingUrl = y['class_levels']['url']
	driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
	driver.get(f"https://www.dnd5eapi.co{levellingUrl}")
	body2 = driver.find_element_by_xpath('/html/body/pre').text
	y2 = json.loads(body2)

	level_list = []
	level_list2 = []
	level_list3 = []
	for i in range(0, 23):
		try:
			valueLevel1 = [y2[i]['features'][x]['name'] for x in range(len(y2[i]['features']))]
		except:
			for i in range(0, 20):
				valueLevel1 = [y2[i]['features'][x]['name'] for x in range(len(y2[i]['features']))]
		valueLevel2 = [y2[i]['feature_choices'][x]['name'] for x in range(len(y2[i]['feature_choices']))]
		valueLevel2 += '\n'
		valueLevel1 = str(f"Level {y2[i]['level']} -> ") + (', ').join(p for p in valueLevel1) + " " + (', ').join(p for p in valueLevel2)
		if 'ability_score_bonuses' in y2[i]:
			valueLevel3 = f"Level {y2[i]['level']} -> {y2[i]['ability_score_bonuses']}"
			level_list2.append(valueLevel3)
		if 'prof_bonus' in y2[i]:
			valueLevel4 = f"Level {y2[i]['level']} -> {y2[i]['prof_bonus']}"
			level_list3.append(valueLevel4)
		level_list.append(valueLevel1)

	level_list = '\n'.join(p for p in level_list)
	level_list2 = '\n'.join(p for p in level_list2)
	level_list3 = '\n'.join(p for p in level_list3)
	return level_list, level_list2, level_list3