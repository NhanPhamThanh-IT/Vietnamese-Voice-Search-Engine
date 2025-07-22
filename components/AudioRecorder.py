import streamlit as st
import speech_recognition as sr

class AudioRecorder:
    @staticmethod
    def render():
        audio_value = st.audio_input("Nhấn để bắt đầu ghi âm")

        if audio_value:
            st.audio(audio_value, format="audio/wav")

            recognizer = sr.Recognizer()
            with sr.AudioFile(audio_value) as source:
                audio_data = recognizer.record(source)

            try:
                text = recognizer.recognize_google(audio_data, language="vi-VN")
                return text
            except Exception as e:
                st.error(f"Lỗi nhận diện giọng nói: {e}")
                return None
