#!/usr/bin/python3

import pprint
import sys
import time

import spotipy
import spotipy.util as util

import config

token = util.prompt_for_user_token(api_user, scope='user-read-currently-playing user-read-playback-state user-modify-playback-state', client_id=api_id, client_secret=api_secret, redirect_uri='https://localhost/asd' )

if token:
	sp = spotipy.Spotify(auth=token)
	while True:
		playing = sp.currently_playing()
		if not playing.get('is_playing'):
			time.sleep(30)
			continue
		artists = playing.get('item',{}).get('artists',[])
		for a in artists:
			if a.get('name') in blocklist:
				print('{} matched block list, skipping'.format(a.get('name')))
				sp.next_track()
				break
		time.sleep(7)
else:
	print("Can't get token for", api_user)
