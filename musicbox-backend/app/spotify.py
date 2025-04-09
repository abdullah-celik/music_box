import requests
from app.config import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

def get_access_token():
    url = "https://accounts.spotify.com/api/token"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }
    data = {
        "grant_type": "client_credentials",
        "client_id": SPOTIFY_CLIENT_ID,
        "client_secret": SPOTIFY_CLIENT_SECRET
    }
    response = requests.post(url, headers=headers, data=data)
    return response.json().get("access_token")

def get_artist(artist_id):
    token = get_access_token()
    response = requests.get(
        f"https://api.spotify.com/v1/artists/{artist_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    return response.json()

def search_albums(query: str):
    try:
        token = get_access_token()
        url = "https://api.spotify.com/v1/search"
        headers = {"Authorization": f"Bearer {token}"}
        #"Authorization": f"Bearer {token}"
        params = {
            "q": query,
            "type": "album",
            "limit": 10,
            "market": "US"
        }
        
        # Add debug logging
        print(f"Making request to Spotify API with token: {token[:15]}...")
        
        response = requests.get(url, headers=headers, params=params)
        
        # Check for HTTP errors
        response.raise_for_status()
        
        data = response.json()
        
        # Verify response structure
        if not data.get('albums'):
            raise ValueError("Unexpected API response format - missing 'albums' key")
            
        return {
            "albums": {
                "items": data['albums'].get('items', []),
                "total": data['albums'].get('total', 0)
            }
        }
        
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        print(f"Response content: {http_err.response.text}")
        raise HTTPException(
            status_code=http_err.response.status_code,
            detail=f"Spotify API error: {http_err.response.text}"
        )

        
def get_album(album_id):
    token = get_access_token()
    response = requests.get(
        f"https://api.spotify.com/v1/albums/{album_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    data = response.json()

    return {
        "name": data["name"],
        "release_date": data["release_date"],
        "label": data.get("label"),
        "total_tracks": data["total_tracks"],
        "images": data["images"],
        "artists": data["artists"],
        "tracks": [
            {
                "name": track["name"],
                "duration_ms": track["duration_ms"],
                "track_number": track["track_number"],
                "preview_url": track["preview_url"]
            } for track in data["tracks"]["items"]
        ]
    }

def get_new_releases():
    token = get_access_token()
    response = requests.get(
        "https://api.spotify.com/v1/browse/new-releases?limit=10",
        headers={"Authorization": f"Bearer {token}"}
    )
    return response.json()

