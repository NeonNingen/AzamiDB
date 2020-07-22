from AzamiDX.core.setup import create_bot, heroku_check

if __name__ == '__main__': # Readding Reconnect
	azami = create_bot()
	token = heroku_check()
	azami.run(token, bot=True, reconnect=True)
