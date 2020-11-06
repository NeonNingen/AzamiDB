import json
from random import choice

def __file_open(file, json_detc: bool):
	with open(f'AzamiDX/etc/img/files/{file}') as f:
		if json_detc == True:
			data = json.load(f)
		else:
			data = f.readlines()

	if json_detc == True:
		pass
	else:
		data = [i.strip() for i in data]
	return data

def rollimg(num):
	data = __file_open('rollimg.txt', False)
	if 0 < num < 9: return data[num-1]

def diceimg(num):
	data = __file_open('diceimg.txt', False)
	if num == 1: return data[0]
	if 1 < num < 7 : return f'https://dobbelsteen.virtuworld.net/img/{num}.gif'
	if 6 < num < 21: return data[num-6]
	if num == i: return data[i-1]

def slapimg(num):
	data = __file_open('slap.json', True)
	if 0 < num < 3: return data['Azami'][num-1]
	if 3 < num < 6: return data['Self'][num-4]
	if num == 7: return choice(data['Others'])

def shootimg(num):
	data = __file_open('shoot.json', True)
	if num == 1: return choice(data['Azami'])
	if num == 2: return choice(data['Self'])
	if num == 3: return choice(data['Others'])
def rpsimg(num):
	data = __file_open('rps.json', True)
	if num == 1: return choice(data['Default'])
	if num == 2: return choice(data['Rock'])
	if num == 3: return choice(data['Paper'])
	if num == 4: return choice(data['Scissors'])
	if num == 5: return choice(data['Winner'])
	if num == 6: return choice(data['Loser'])
	if num == 7: return choice(data['Tie'])

def nagoombaimg(word):
	data = __file_open('nagoomba_image.json', True)
	return data[word.upper()]