
# 🎵 MusicBox

A full-stack music discovery application that connects to the Spotify API to browse and search albums.

![MusicBox Screenshot](./screenshot.png)

## ✨ Features
- 🔍 Search Spotify's album catalog
- 🆕 Browse new releases
- 📄 View detailed album information
- 🎨 Responsive UI with clean design

## 🛠️ Setup

### Prerequisites
- Python 3.8+
- Node.js 14+
- Spotify Developer Account ([create one here](https://developer.spotify.com/dashboard))
- Git

### 1. Clone Repository
git clone git@github.com:abdullah-celik/musicbox.git
cd musicbox

2. Backend Setup
bash
Copy

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Configure environment
echo "SPOTIFY_CLIENT_ID=your_client_id" > .env
echo "SPOTIFY_CLIENT_SECRET=your_client_secret" >> .env

# Run backend (http://localhost:8000)
uvicorn main:app --reload

3. Frontend Setup
bash
Copy

cd musicbox-frontend

# Install dependencies
npm install

# Configure environment
echo "REACT_APP_API_URL=http://localhost:8000" > .env

# Run frontend (http://localhost:3000)
npm start

⚙️ Configuration
Spotify API

    Create an app at Spotify Developer Dashboard

    Add http://localhost:8000 to Redirect URIs

    Copy your Client ID and Secret to .env

Environment Files

Backend (musicbox/.env)
Copy

SPOTIFY_CLIENT_ID=your_client_id_here
SPOTIFY_CLIENT_SECRET=your_client_secret_here

Frontend (musicbox-frontend/.env)
Copy

REACT_APP_API_URL=http://localhost:8000

🌐 API Endpoints
Endpoint	Method	Description	Example
/search/album?query={name}	GET	Search albums	/search/album?query=thriller
/new-releases	GET	Get new releases	/new-releases
/album/{id}	GET	Get album details	/album/4aawyAB9vmqN3uQ7FjRGTy
🏗️ Project Structure
Copy

musicbox/
├── main.py               # FastAPI application
├── spotify.py            # Spotify API service
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables

musicbox-frontend/
├── src/
│   ├── pages/            # React pages (Home, etc.)
│   ├── components/       # Reusable components
│   ├── App.js            # Main component
│   └── index.js          # Entry point
├── public/               # Static assets
└── package.json          # Frontend dependencies

🚀 Deployment
Backend (Example for Vercel)
bash
Copy

pip install fastapi[all]
vercel --prod

Frontend
bash
Copy

npm run build
vercel --prod

🤝 Contributing

    Fork the project

    Create your feature branch (git checkout -b feature/AmazingFeature)

    Commit your changes (git commit -m 'Add some feature')

    Push to the branch (git push origin feature/AmazingFeature)

    Open a Pull Request

📜 License

MIT License - see LICENSE for details.
📬 Contact

Abdullah Celik
📧 abdullah@example.com
🐦 @abdullah_dev
🔗 https://github.com/abdullah-celik

    Note: Replace all placeholder values (your credentials, contact info) before using.
    Add a project screenshot named screenshot.png in your root directory.

Copy


### How to Use:
1. Copy this entire content
2. Create a new file named `README.md` in your project root
3. Paste the content
4. Replace all placeholder values (credentials, contact info)
5. Save your screenshot as `screenshot.png` in the root folder
6. Commit to GitHub:
```bash
git add README.md screenshot.png
git commit -m "Add comprehensive README"
git push origin main# music_box
