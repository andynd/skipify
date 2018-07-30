#!/usr/bin/python3

import sys
import time

import spotipy
import spotipy.util as util

from config import *

print('Skipping the following artists: {}'.format(blocklist.get('artist.name')))
while True:
	try:
		token = util.prompt_for_user_token(api_user, scope='user-read-currently-playing user-read-playback-state user-modify-playback-state', client_id=api_id, client_secret=api_secret, redirect_uri='https://localhost/asd' )
		if token:
			print('Refreshed spotify auth token')
			sp = spotipy.Spotify(auth=token)
			while True:
				playing = sp.currently_playing()
				if not playing or not playing.get('is_playing'):
					time.sleep(30)
					continue
				song = playing.get('item',{})
				artists = song.get('artists',[])
				skipped = False
				for artist in artists:
					if artist.get('name') in blocklist.get('artist.name', []):
						print('"{}" matched block list, skipping "{}"'.format(artist.get('name'), song.get('name')))
						sp.next_track()
						skipped = True
						break
				if skipped:
					time.sleep(1)
				else:
					time.sleep(7)
		else:
			print("Can't get token for", api_user)
			exit(1)
	except spotipy.client.SpotifyException:
		time.sleep(5)
		pass
