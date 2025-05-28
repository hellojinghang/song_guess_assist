# 🎵 Song Guess Assistance Game (Streamlit App)

This app helps users practice guessing songs by playing a random part of a YouTube song.

## Features
- Paste a YouTube link.
- Choose how many seconds to play.
- App plays a random audio snippet from the song.
- Download snippet to guess later.

## Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
```

Make sure `ffmpeg` is installed for audio slicing:
- Windows: https://ffmpeg.org/download.html
- Mac: `brew install ffmpeg`
- Linux: `sudo apt install ffmpeg`

## Deploy Online (Streamlit Cloud)
1. Push this project to a GitHub repository.
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Click "New App", select your repo and branch.
4. Set the Python file as `app.py` and deploy.
