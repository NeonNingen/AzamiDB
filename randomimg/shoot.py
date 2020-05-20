from random import choice

def shoot():
	shoot_list = [
	"http://static1.comicvine.com/uploads/original/11127/111275532/5288551-9830962548-latest",
	"http://i.imgur.com/hPL5TGD.gif"
	]
	shoot_img = choice(shoot_list)
	return shoot_img
