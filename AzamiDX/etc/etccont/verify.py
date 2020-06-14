import discord

def verify(azami, channel, member):
	rules = azami.get_channel(718406709814624288)
	hub = azami.get_channel(699998325113356388)
	makers = azami.get_channel(718286296849842278)
	msg = (
		f"""
Welcome to **{channel.guild}!**
Greeting from all of us aboard the starship!

➤ Make sure to read: {rules.mention}

➤ Come and hangout in the startship!
⠀⠀ at the: {hub.mention}

➤ Need support or have queries about Azami.
   Go to the 𝐂𝐡𝐨𝐦𝐩𝐰𝐨𝐫𝐤𝐬 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐚𝐥𝐚𝐱𝐲 Category

➤ Wanna test your own bot? 
   Try it out at {makers.mention}

➤ Wanna get free games or talk about anime? 
   Check out the 𝐒𝐮𝐩𝐞𝐫𝐦𝐚𝐬𝐬𝐢𝐯𝐞 𝐆𝐚𝐥𝐚𝐱𝐲 Category!

*May the stars shine down on you*
{member.mention}, Please react with :white_check_mark: to verify!
		 """)
	return msg