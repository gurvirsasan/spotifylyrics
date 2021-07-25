SPOTIFYLYRICS

Program has been tested for macOS

First, you would need to create a spotipy and genius api account. From there, access SPOTIPY_CLIENT_ID, SPOTIPY_CLIENT_SECRET, GENIUS_ACCESS_TOKEN.

Once acquired, replace them on the right side of the equal sign and run the following commands in terminal: 


export SPOTIPY_CLIENT_ID='' 
export SPOTIPY_CLIENT_SECRET=''
export SPOTIPY_REDIRECT_URI='https://google.com'
export GENIUS_ACCESS_TOKEN=''

You can run `automate_lyrics.py` now and it should provide lyrics for the song that you’re playing and should update with every song that is changed.
