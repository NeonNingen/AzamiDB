import discord
from random import choice
from AzamiDX.etc.img.display import *
from AzamiDX.core.utils import color_list, pre_embed
from AzamiDX.etc.etccont.colorchoice import color_choice

def slapper(ctx):

	slap_arr = ['Take that sucker!', 'This is gonna hurt!', 'You really make me angry!',
				"I'll smack you to oblivion", 'One and two and SLAP!', 'SLAP SLAP SLAP',
				'Slapping is my middle name', "Now that's alot of damage", 'Gonna cry?']

	store_dict = {'azami': {1: {'title': 'Why am I slapping myself!?',
								'desc': 'How could you!',
								'color': discord.Color.blue(),
								'url': slapimg(1)},
							2: {'title': 'My head!',
								'desc': 'Slapped against the wall...',
								'url': slapimg(2)}},

				  'self': {1: {'title': 'Haha Why you slapping yourself, why you slapping yourself',
							   'desc': 'How could you!',
							   'color': discord.Color.red(),
							   'url': slapimg(4)},
						   2: {'title': 'My head!',
							   'desc': 'Slapped against the wall...',
							   'url': slapimg(5)}},

				  'others': {'title': choice(slap_arr),
					  		 'desc': f'You were slapped by {ctx.author.mention}',
					  		 'url': slapimg(7)}}

	return store_dict

def shoot(member, ctx):

	shoot_arr_azami = ['Dodged it!', 'That was close', 
					   "You aren't such a sharp shot, after all",
					   'I can do this all day!', 'Bullets are pointless',
					   'Put your back into it!']

	shoot_arr_self = ['You died! Better luck next time!', 'RIP', "F's in the chat bois",
					  'Ouch', "Well dying isn't so bad",
					  'What did it cost... Everything',
					  'What was the point in that? What were you trying to prove?',
					  'L', 'Oof']

	shoot_arr_other = ["It's a hit!", 'Moving is futile!', "You can't escape me!",
				 	   "Try dodging this!, spoiler: you can't",
				 	   'Death is such sweet sorrow',
				 	   'This is gonna be quick if you stay still!', 
				 	   "I'll end your suffering","Go out quietly or don't", 
				 	   'You lose', 'Die!']

	store_dict = {'azami': {'title': choice(shoot_arr_azami),
							'desc': f'You attempted to shoot me {ctx.author.mention}, but I dodged it!',
							'color': discord.Color.green(),
							'url': shootimg(1)},

				  'self':  {'title': choice(shoot_arr_self),
				  			'desc': f"{ctx.author.name} committed suicide!",
				  			'color': discord.Color.red(),
				  			'url': shootimg(2)},

				  'others': {'title': choice(shoot_arr_other),
					  		 'desc': f'{member.name} was shot dead by the mighty {ctx.author.name}',
					  		 'url': shootimg(3)}}

	return store_dict

def rockpapsci(ctx):

	rps_arr_start = ["Let's start the game!", "Let's play Rock, paper, scissors!",
					 'You up for a match?', 'This will be the battle of your life!']

	rps_arr_winner = ['Winner Winner Chicken Dinner!', 'Congratulations',
					  'Great Success, you win!', 'You beat me!?',
					  'I guess I lost this time, well done!', 'Please fight me again! You win!']

	rps_arr_loser = ['The loser is... YOU!', 'Haha better luck next time!',
					 'Get serious, baka!', 'Pft, so pathetic', 'You lose!',
					 'Maybe try harder next time',
					 'Of course I would never lose against someone of the likes you!']

	rps_arr_tie = ["You... you're not so bad...", "I'll win next time!",
				   'The fights not over', 'You drew', "It's a tie...",
				   "This isn't how it's suppose to end! Show me more!"]

	store_dict = {'default': {'title': f'Hello {ctx.message.author.name}',
							  'desc': choice(rps_arr_start),
							  'url': rpsimg(1),
							  'footer': 'Wins, ties and loses shown here!'},

				  'r': {1: {'title': 'You threw out a rock',
				  			'desc': 'Rock against...',
				  			'color': discord.Color.dark_grey(),
				  			'url': rpsimg(2),
				  			'beats': 's'},
				  		2: {'title': 'Rock!',
				  			'url': rpsimg(2)}},

				  'p': {1: {'title': 'You hit me with paper',
				  			'desc': 'Paper against...',
				  			'color': discord.Color.lighter_grey(),
				  			'url': rpsimg(3),
				  			'beats': 'r'},
				  		2: {'title': 'Paper!',
				  			'url': rpsimg(3)}},

				  's': {1: {'title': 'You slashed out some scissors',
				  			'desc': 'Scissors against...',
				  			'color': discord.Color.gold(),
				  			'url': rpsimg(4),
				  			'beats' : 'p'},
				  		2: {'title': 'Scissors!!',
				  			'url': rpsimg(4)}},

				  'end': {'winner': {'title': choice(rps_arr_winner),
				  					 'color': discord.Color.green(),
				  					 'url': rpsimg(5)},

				  		  'loser': {'title': choice(rps_arr_loser),
				  		  			'color': discord.Color.red(),
				  		  			'url': rpsimg(6)},

				  		  'tie': {'title': choice(rps_arr_tie),
				  		  		  'color': discord.Color.blue(),
				  		  		  'url': rpsimg(7)}}}

	return store_dict

def customem(ctx):

	store_dict = {'1⃣': {'title': 'Please enter the title of the embed below!',
					    'desc': 'Below shows an example of a title for your embed!',
					    'url': 'https://i.imgur.com/loHwQXJ.png'},
				  '2⃣': {'title': 'Please enter the description of the embed below!',
					    'desc': 'Below shows an example of a description for your embed!',
					    'url': 'https://i.imgur.com/Qpbewle.png'},
				  '3⃣': {'title': 'Please enter the color of the embed below!',
					    'desc': 'Write the num for the color!\nBelow is the list of colors with the num to select!',
					    'url': 'https://i.imgur.com/52IM4h1.png'},
				  '4⃣': {'title': 'Please enter the thumbnail of the embed below!',
					    'desc': 'Below shows an example of a thumbnail for your embed!',
					    'url': 'https://i.imgur.com/rMBwBAE.png'},
				  '5⃣': {'title': 'Please enter the image of the embed below!',
					    'desc': 'Below shows an example of an image for your embed!',
					    'url': 'https://i.imgur.com/yNM04FO.png'},
				  '6⃣': {'title': 'Please enter the footer text of the embed below!',
					    'desc': 'Below shows an example of a footer text for your embed!',
					    'url': 'https://i.imgur.com/sMBgrrX.png'},
				  '7⃣': {'title': 'Please enter the footer image of the embed below!',
					    'desc': 'Below shows an example of a footer image for your embed!',
					    'url': 'https://i.imgur.com/V3xyWNr.png'},
				  '8⃣': {'title': 'Please enter the number of fields below!',
					    'desc': 'This way we know which fields you want.\n'\
					     		'Below is an example of fields!',
					    'url': 'https://i.imgur.com/D7d6V2d.png'}}

	return store_dict

async def final_embed(ctx, list_var: dict, field_name: list, field_value: list):

	if '1⃣' in list_var:
		titl = list_var.get('1⃣')
	else:
		titl = ''

	if '2⃣' in list_var:
		desc = list_var.get('2⃣')
	else:
		desc = ''

	if '3⃣' in list_var:
		try:
			color = list_var.get('3⃣')
			color = color_choice(color)
		except:
			color = color_list()
	else:
		color = color_list()

	if '4⃣' in list_var:
		thumbnail = list_var.get('4⃣')
	else:
		thumbnail = ''

	if '5⃣' in list_var:
		image_url = list_var.get('5⃣')
	else:
		image_url = ''

	if '6⃣' in list_var:
		footer_text = list_var.get('6⃣')
	else:
		footer_text = ''

	if '7⃣' in list_var:
		footer_img = list_var.get('7⃣')
	else:
		footer_img = ''

	if '8⃣' in list_var:
		fields = field_name
		values = field_value
		num = len(field_name)
	else:
		fields = []
		values = []
		num = 0

	em = await pre_embed(titl=titl,
				   		 desc=desc,
				   		 color=color,
				   		 thumb_url=thumbnail,
				   		 image_url=image_url,
				   		 foot_txt=footer_text,
				   		 foot_url=footer_img,
				   		 ctx=ctx,
				   		 num=num,
				   		 fields=fields,
				   		 values=values)

	return em

	
