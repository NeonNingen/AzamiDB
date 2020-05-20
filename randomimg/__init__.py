from random import randint, choice

def slap():
	slap_list = [
	'https://media.giphy.com/media/l3vRb8wtvRtW9mOk0/giphy.gif',
	'https://media.giphy.com/media/l1IYa5UYE8iBLWp6E/giphy.gif',
	'https://media0.giphy.com/media/xUPGcF8xjWmt2CRuo0/giphy.gif',
	'https://media1.giphy.com/media/JBsgmn8uGR5hm/giphy.gif'
	]
	return slap_list[randint(0,2)]

def shoot():
	shoot_list = [
	"http://static1.comicvine.com/uploads/original/11127/111275532/5288551-9830962548-latest",
	"http://i.imgur.com/hPL5TGD.gif"
	]
	shoot_img = choice(shoot_list)
	return shoot_img