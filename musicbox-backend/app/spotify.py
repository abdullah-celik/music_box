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

"""def search_albums(query: str):
    url = f"https://api.spotify.com/v1/search"
    headers = {"Authorization": get_access_token()}
    params = {
        "q": query,
        "type": "album",
        "limit": 10,
    }
    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    albums = []
    for item in data.get("albums", {}).get("items", []):
        albums.append({
            "name": item["name"],
            "artist": item["artists"][0]["name"],
            "image": item["images"][0]["url"] if item["images"] else None,
            "spotify_url": item["external_urls"]["spotify"],
            "release_date": item["release_date"]
        })

    return {"albums": albums}"""
    
def search_albums(query: str):
    try:
        token = get_access_token()
        url = "https://api.spotify.com/v1/search"
        headers = {"Authorization": get_access_token()}
        params = {
            "q": query,
            "type": "album",
            "limit": 10,
            "market": "US"
        }
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        data = response.json()
        
        return {
            "albums": {
                "items": data.get("albums", {}).get("items", []),
                "total": data.get("albums", {}).get("total", 0)
            }
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

def get_album(album_id):
    token = get_access_token()
    response = requests.get(
        f"https://api.spotify.com/v1/albums/{album_id}",
        headers={"Authorization": f"Bearer {token}"}
    )
    return response.json()

def get_new_releases():
    token = get_access_token()
    response = requests.get(
        "https://api.spotify.com/v1/browse/new-releases?limit=10",
        headers={"Authorization": f"Bearer {token}"}
    )
    return response.json()

