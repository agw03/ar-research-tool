import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

def verify_artist(artist_name):
    verify = sp.search(q=artist_name, type="artist", limit=1)
    if not verify["artists"]["items"]:
        return None
    else:
        return verify["artists"]["items"][0]["name"]

load_dotenv()

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

auth_manager = SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret,
)

sp = spotipy.Spotify(auth_manager=auth_manager)

# results = sp.search(q="Arlo Parks", type="artist", limit=1)
# full_artist = results["artists"]["items"][0]
# print(full_artist.keys())
