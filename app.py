import streamlit as st
import requests
from components import LeftSidebar, PageHeader, AudioRecorder, AudioPlayer
from utils import Scrapper
from settings import ThemeManager, AppConfig

ThemeManager.apply()

class RightColumn:
    @staticmethod
    def render():
        _, col, _ = st.columns([1, 10, 1])
        with col:
            RightColumn.render_main_content()

    @staticmethod
    def render_main_content():
        PageHeader.render(
            title=AppConfig.APP_HEADER["TITLE"],
            description=AppConfig.APP_HEADER["DESCRIPTION"]
        )

        query = AudioRecorder.render()

        if query:
            if "played_intro" not in st.session_state:
                AudioPlayer.render("Bắt đầu xử lý...", state_key="played_intro")
                return

            if "played_result" not in st.session_state:
                with st.spinner("Đang xử lý..."):
                    response = Scrapper.get_serper_news(query)
                    if isinstance(response, requests.Response):
                        url = Scrapper.get_url_from_response(response)
                        summary = Scrapper.summarize_from_url(url)
                        result = Scrapper.preprocess_text(summary)
                        AudioPlayer.render(result, state_key="played_result")
                        return

            else:
                del st.session_state.played_intro
                del st.session_state.played_result


class MainApp:
    def __init__(self):
        self.left_sidebar = LeftSidebar()
        self.right_column = RightColumn()

    def run(self):
        self.set_page_config()

        self.left_sidebar.render()
        self.right_column.render()

    def set_page_config(self):
        st.set_page_config(
            page_title=AppConfig.APP_HEADER["TITLE"],
            layout="wide",
            initial_sidebar_state="expanded",
            page_icon=":mag_right:"
        )

if __name__ == "__main__":
    app = MainApp()
    app.run()
