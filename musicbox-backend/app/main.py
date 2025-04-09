from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware  # 🧩 Import CORS middleware
from app.spotify import search_albums, get_album, get_new_releases
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Now, you can access the client ID and secret
client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')

# Create Spotify client
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

# You must have SPOTIPY_CLIENT_ID and SPOTIPY_CLIENT_SECRET set in your .env or OS environment
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

app = FastAPI(title="MusicBox API")

# 🔐 Add CORS middleware (this allows your frontend to access the API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Or use ['http://localhost:3000'] for more secure dev setup
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Welcome to MusicBox 🎵"}


"""@app.get("/album/{album_id}")
def album(album_id: str):
    return get_album(album_id)"""
@app.get("/search/album")
async def search_album_endpoint(query: str):
    try:
        results = search_albums(query)
        return results
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/new-releases")
def new_releases():
    return get_new_releases()

@app.get("/artist/{artist_id}")
def artist(artist_id: str):
    return get_artist(artist_id)
@app.get("/album/{album_id}")
def get_album(album_id: str):
    album = sp.album(album_id)  # using Spotipy client
    return album
