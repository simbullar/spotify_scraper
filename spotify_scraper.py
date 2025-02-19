import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
cid = ''
secret = ''

scope = 'user-library-read'
with open("songs.txt", "w") as song:
    song.close()

def show_tracks(results):
    for item in results['items']:
        track = item['track']
        songs = (track['name'])
        with open("songs.txt", "a") as song:
            song.write(songs + "\n")


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, client_id=cid, client_secret=secret, redirect_uri="http://localhost:3000"))

results = sp.current_user_saved_tracks()
show_tracks(results)

while results['next']:
    results = sp.next(results)
    show_tracks(results)





