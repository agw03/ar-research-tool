import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import os

load_dotenv()

client_id = os.getenv("SPOTIFY_CLIENT_ID")
client_secret = os.getenv("SPOTIFY_CLIENT_SECRET")

auth_manager = SpotifyClientCredentials(
    client_id=client_id,
    client_secret=client_secret,
)

sp = spotipy.Spotify(auth_manager=auth_manager)

results = sp.search(q="Arlo Parks", type="artist", limit=1)
full_artist = results["artists"]["items"][0]
print(full_artist.keys())

#artist_detail = sp.artist("4kIwETcbpuFgRukE8o7Opx")
#print(artist_detail.keys())
#artist_detail = sp.artist(first["id"])
#print(artist_detail["name"])
#print(artist_detail["followers"]["total"])
#print(artist_detail["popularity"])
#print(artist_detail["genres"])
