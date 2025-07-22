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
            AudioPlayer.render("Đang tìm kiếm thông tin...")
            response = Scrapper.get_serper_news(query)
            if isinstance(response, requests.Response):
                url = Scrapper.get_url_from_response(response)
                summary = Scrapper.summarize_from_url(url)
                result = Scrapper.preprocess_text(summary)
                AudioPlayer.render(result)

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
