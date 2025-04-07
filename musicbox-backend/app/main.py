from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware  # 🧩 Import CORS middleware
from app.spotify import search_albums, get_album, get_new_releases
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

"""# Should be (add response model):
@app.get("/search/album", response_model=dict)
async def search_albums(query: str):
    try:
        results = search_albums(query)  # Your actual search function
        return {"albums": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
@app.get("/album/{album_id}")
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

