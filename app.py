
import streamlit as st
from pytube import YouTube
from pydub import AudioSegment
import random
import os
import uuid

st.set_page_config(page_title="🎵 Song Guess Game", layout="centered")
st.title("🎵 Song Guess Assistance Game")

yt_url = st.text_input("Paste a YouTube Song URL here:")

if yt_url:
    try:
        yt = YouTube(yt_url)
        title = yt.title
        st.success(f"Loaded: {title}")
        audio_stream = yt.streams.filter(only_audio=True).first()

        if st.button("Download and Prepare Audio"):
            audio_file_path = f"{uuid.uuid4()}.mp4"
            audio_stream.download(filename=audio_file_path)
            st.session_state["audio_path"] = audio_file_path

    except Exception as e:
        st.error(f"Error loading video: {e}")

if "audio_path" in st.session_state:
    seconds = st.slider("Choose how many seconds to play:", 3, 30, 10)

    audio = AudioSegment.from_file(st.session_state["audio_path"])
    duration_ms = len(audio)

    if st.button("🎧 Play Random Snippet"):
        start_ms = random.randint(0, duration_ms - (seconds * 1000))
        snippet = audio[start_ms:start_ms + seconds * 1000]

        snippet_path = f"snippet_{uuid.uuid4()}.mp3"
        snippet.export(snippet_path, format="mp3")
        st.audio(snippet_path)

        st.session_state["last_snippet"] = snippet_path

    if "last_snippet" in st.session_state:
        st.download_button("⬇ Download Snippet", data=open(st.session_state["last_snippet"], "rb"), file_name="guess_snippet.mp3")

if st.button("Reset Game"):
    for key in ["audio_path", "last_snippet"]:
        if key in st.session_state and os.path.exists(st.session_state[key]):
            os.remove(st.session_state[key])
        st.session_state.pop(key, None)
    st.experimental_rerun()
