import requests
from components import PageHeader, AudioRecorder, AudioPlayer
from utils import Scrapper
from settings import ThemeManager
from config import TITLE, DESCRIPTION

ThemeManager.apply()

PageHeader.render(TITLE, DESCRIPTION)

query = AudioRecorder.render()

if query:
    AudioPlayer.render("Đang tìm kiếm thông tin...")
    response = Scrapper.get_serper_news(query)
    if isinstance(response, requests.Response):
        url = Scrapper.get_url_from_response(response)
        summary = Scrapper.summarize_from_url(url)
        result = Scrapper.preprocess_text(summary)
        AudioPlayer.render(result)