import discord

def verify(azami, channel, member):
	rules = azami.get_channel(699997840985948222)
	hub = azami.get_channel(699998325113356388)
	msg = (
		f"""
Welcome to **{channel.guild}!**
Greeting from all of us aboard the starship!

➤ Make sure to read: {rules.mention}

➤ Come and hangout in the startship!
   at the: {hub.mention}

➤ Wanna get free games or talk about anime? 
   Check out the 𝐒𝐮𝐩𝐞𝐫𝐦𝐚𝐬𝐬𝐢𝐯𝐞 𝐆𝐚𝐥𝐚𝐱𝐲 Category!

*May the stars shine down on you*
{member.name}, Please react with :white_check_mark: to verify!
		 """)
	return msg
