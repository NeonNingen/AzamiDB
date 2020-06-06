import discord, lavalink, re
from discord.ext import commands
from AzamiDX.core.utils import edit

url_rx = re.compile(r'https?://(?:www\.)?.+')

class Music(commands.Cog):

	def __init__(self, azami):
		self.azami = azami

		self.azami.music = lavalink.Client(self.azami.user.id)
		self.azami.music.add_node('localhost', 7000, 'testing', 'na', 'music-node')
		self.azami.add_listener(self.azami.music.voice_update_handler, 'on_socket_response')
		
		self.azami.music.add_event_hook(self.track_hook)

	def cog_unload(self):
		self.azami.music._event_hooks.clear()

	async def cog_before_invoke(self, ctx):
		guild_check = ctx.guild is not None

		if guild_check:
			await self.ensure_voice(ctx)

		return guild_check
	
	async def cog_command_error(self, ctx, error):
		if isinstance(error, commands.CommandInvokeError):
			await ctx.send(error.original)

	async def track_hook(self, event):
		if isinstance(event, lavalink.events.QueueEndEvent):
			guild_id = int(event.player.guild_id)
			await self.connect_to(guild_id, None)

	async def connect_to(self, guild_id: int, channel_id: str):
		ws = self.azami._connection._get_websocket(guild_id)
		await ws.voice_state(str(guild_id), channel_id)

	async def ensure_voice(self, ctx):
		player = self.azami.music.player_manager.create(ctx.guild.id, endpoint=str(ctx.guild.region))

		should_connect = ctx.command.name in ('play',)
		vc = ctx.author.voice

		if not vc or not vc.channel:
			raise commands.CommandInvokeError('Join a voicechannel first')

		if not player.is_connected:
			if not should_connect:
				raise commands.CommandInvokeError('Not connected')

			permissions = vc.channel.permissions_for(ctx.me)

			if not permissions.connect or not permissions.speak:
				raise commands.CommandInvokeError('I need the CONNECT and SPEAK permissions')

			player.store('channel', ctx.channel.id)
			await self.connect_to(ctx.guild.id, str(vc.channel.id))
		else:
			if int(player.channel_id) != vc.channel.id:
				raise commands.CommandInvokeError('You need to be in my voicechannel')

	@commands.command(description="Let's play some music")
	async def play(self, ctx, *, query): # Add Pause, stop, dc and ensure_voice check
		def check(m):
			return m.author == ctx.author and m.channel == ctx.channel
		j = 0
		while True:
			j += 1
			player = self.azami.music.player_manager.get(ctx.guild.id)
			query = query.strip('<>')

			if not url_rx.match(query):
				query = f'ytsearch:{query}'

			results = await player.node.get_tracks(query)

			if not results or not results['tracks']:
				await ctx.send(f"Nothing was found! Occured {j} time(s), trying again.")
				if j == 10:
					await ctx.send("Ultimatly nothing was found")
					return
			else:
				break
		em = discord.Embed(color=discord.Color.blurple())

		if results['loadType'] == 'TRACK_LOADED':
			 track = results['tracks'][0]
			 em.title = 'Track Loaded!'
			 em.description = f'[{track["info"]["title"]}]({track["info"]["uri"]})'

			 await ctx.channel.send(embed=em)

			 player.add(requester=ctx.author.id, track=track)
			 if not player.is_playing:
			 	await player.play()

		if results['loadType'] == 'PLAYLIST_LOADED':
			tracks = results['tracks']
			for track in tracks:
				player.add(requester=ctx.author.id, track=track)
			em.title = 'Playlist Loaded!'
			em.description = f'{results["playlistInfo"]["name"]} - {len(tracks)} tracks'

			await ctx.channel.send(embed=em)

			player.add(requester=ctx.author.id, track=track)
			if not player.is_playing:
				await player.play()

		if results['loadType'] == 'SEARCH_RESULT':
			tracks = results['tracks'][0:10]
			i = 0
			query_result = ''
			for track in tracks:
				i += 1
				query_result = query_result + f'{i}) {track["info"]["title"]} - {track["info"]["uri"]}\n'
		
			em.description = query_result

			await ctx.channel.send(embed=em)
			await ctx.send(f"Please select a song or write q to quit, {ctx.author.mention}!")

			response = await self.azami.wait_for('message', check=check)

			if response.content == "q":
				await edit(ctx, content='See you next time!')
				return
			else:
				try:
					track = tracks[int(response.content) - 1]
					em.title = 'Track Loaded!'
					em.description = f'[{track["info"]["title"]}]({track["info"]["uri"]})'
					await ctx.send(embed=em)
					player.add(requester=ctx.author.id, track=track)
					if not player.is_playing:
						await player.play()
				except:
					await edit(ctx, content="Invalid number given", ttl=5)

		if results['loadType'] == 'NO_MATCHES':
			await ctx.channel.send("Error in finding song")

		if results['loadType'] == 'LOAD_FAILED':
			await ctx.channel.send("Failled to play song")

	@commands.command(description="Turn off that racket!")
	async def stop(self, ctx):
		player = self.azami.music.player_manager.get(ctx.guild.id)
		vc = ctx.author.voice

		if not player.is_connected:
			return await ctx.send("Not connected")

		if not vc or (player.is_connected and vc.channel.id != int(player.channel_id)):
			return await ctx.send("You're not in my voicechannel")
		
		if player.is_playing:
			player.queue.clear()
			await player.stop()
			await ctx.send("Music has stopped!")
		elif not player.is_playing:
			await ctx.send("No Music is playing")

	@commands.command(aliases=['dc'], description="Talk to you later!")
	async def disconnect(self, ctx):
		player = self.azami.music.player_manager.get(ctx.guild.id)
		vc = ctx.author.voice

		if not player.is_connected:
			return await ctx.send("Not connected")

		if not vc or (player.is_connected and vc.channel.id != int(player.channel_id)):
			return await ctx.send("You're not in my voicechannel")

		player.queue.clear()
		await player.stop()
		await self.connect_to(ctx.guild.id, None)
		await ctx.send("**Successfully Disconnect!**")


def setup(azami):
	azami.add_cog(Music(azami))
