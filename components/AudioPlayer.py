import streamlit as st
from gtts import gTTS
import tempfile
import os
import time
from mutagen.mp3 import MP3

class AudioPlayer:
    @staticmethod
    def render(text: str, lang: str = "vi", state_key: str = None):
        if not text.strip():
            return

        audio_path = None
        try:
            tts = gTTS(text=text, lang=lang)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tts_fp:
                tts.save(tts_fp.name)
                audio_path = tts_fp.name

            audio_info = MP3(audio_path)
            duration = audio_info.info.length

            with open(audio_path, "rb") as f:
                audio_bytes = f.read()
                st.audio(audio_bytes, format="audio/mp3", autoplay=True)

            if state_key:
                st.session_state[state_key] = True
                time.sleep(duration + 0.5)
                st.rerun()

        finally:
            if audio_path and os.path.exists(audio_path):
                os.remove(audio_path)
