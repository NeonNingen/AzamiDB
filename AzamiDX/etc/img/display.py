def __file_open(file):
	with open(f'AzamiDX/etc/img/{file}') as f:
		data = f.readlines()
	data = [i.strip() for i in data]
	return data

def rollimg(num):
	data = __file_open('rollimg.txt')
	if 0 < num < 9: return data[num-1]

def diceimg(num):
	data = __file_open('diceimg.txt')
	if num == 1: return data[0]
	if 1 < num < 7 : return f'https://dobbelsteen.virtuworld.net/img/{num}.gif'
	if 6 < num < 21: return data[num-6]
	if num == i: return data[i-1]




