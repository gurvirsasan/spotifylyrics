"""
Author: Gurvir Singh Sasan
Creating a web scrapping project that will take songs from spotify
and automatically use Genius.com to scrape the lyrics and display them 
onto the screen.
"""

import os
import json
import spotipy
import time
import lyricsgenius as genius

# store information in environment variables
# export SPOTIPY_CLIENT_ID='ef1d8a4f97f64bb893d8deedd367f1fa'
# export SPOTIPY_CLIENT_SECRET='a1a1204339c74871b0b94c6a01588db9'
# export SPOTIPY_REDIRECT_URI='https://google.com'
# export GENIUS_ACCESS_TOKEN='yrV9GhG6J-To-d4KDD0ZVbwaUuIXHbI1LikQuuZH7kZrk3Hiky1YgtJfqMG_bm6t'

# accessing data from the environment
sp_client_id = os.environ['SPOTIPY_CLIENT_ID']
sp_secret_id = os.environ['SPOTIPY_CLIENT_SECRET']
sp_redirect_uri = os.environ['SPOTIPY_REDIRECT_URI']
genius_access_token = os.environ['GENIUS_ACCESS_TOKEN']

# set the scope for the spotify search
scope = 'user-read-currently-playing'

OAuth = spotipy.SpotifyOAuth(client_id=sp_client_id,
                             client_secret=sp_secret_id,
                             redirect_uri=sp_redirect_uri,
                             scope=scope)
token_dict = OAuth.get_cached_token()
token = token_dict['access_token']

# spotify object
spotify_obj = spotipy.Spotify(auth=token)
# genius object
genius_obj = genius.Genius(genius_access_token)

# getting the song data from spotify
current = spotify_obj.currently_playing()
# print(json.dumps(current, sort_keys=False, indent=4))
artist_name = current['item']['album']['artists'][0]['name']
title = current['item']['name']

# now get the lyrics for this song
