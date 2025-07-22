import streamlit as st
from gtts import gTTS
import tempfile
import os

class AudioPlayer:
    @staticmethod
    def render(text: str, lang: str = "vi"):
        if not text.strip():
            st.warning("Không có nội dung để đọc!")
            return

        audio_path = None
        try:
            tts = gTTS(text=text, lang=lang)
            with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as tts_fp:
                tts.save(tts_fp.name)
                audio_path = tts_fp.name

            with open(audio_path, "rb") as f:
                audio_bytes = f.read()
                st.audio(audio_bytes, format="audio/mp3", autoplay=True)

        except Exception as e:
            st.error(f"Lỗi phát giọng nói!")
        finally:
            if audio_path and os.path.exists(audio_path):
                os.remove(audio_path)