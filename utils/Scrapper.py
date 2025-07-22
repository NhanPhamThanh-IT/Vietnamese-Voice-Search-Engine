import requests
import json
from newspaper import Article
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
from config import SERPER_API_KEY

class Scrapper:
    @staticmethod
    def get_url_from_response(response):
        try:
            news_data = response.json().get('news', [])
            if not news_data:
                return "Không tìm thấy dữ liệu phù hợp."
            new_data = news_data[0]
            new_link = new_data.get('link', '')
            return new_link
        except Exception as e:
            return "Không tìm thấy dữ liệu phù hợp."
        
    @staticmethod
    def get_serper_news(query: str, location: str = "Vietnam", gl: str = "vn", hl: str = "vi") -> str:
        url = "https://google.serper.dev/news"
        headers = {
            'X-API-KEY': SERPER_API_KEY,
            'Content-Type': 'application/json'
        }
        payload = json.dumps({
            "q": query,
            "location": location,
            "gl": gl,
            "hl": hl
        })

        try:
            response = requests.post(url, headers=headers, data=payload)
            response.raise_for_status()
            return response
        except requests.exceptions.HTTPError as http_err:
            return f"Lỗi HTTP: {http_err.response.status_code} - {http_err.response.reason}"
        except requests.exceptions.ConnectionError:
            return "Không thể kết nối tới máy chủ. Vui lòng kiểm tra kết nối mạng."
        except requests.exceptions.Timeout:
            return "Yêu cầu quá thời gian chờ. Vui lòng thử lại sau."
        except requests.exceptions.RequestException as e:
            return f"Đã xảy ra lỗi không xác định: {str(e)}"

    @staticmethod
    def get_article_text(url: str) -> str:
        article = Article(url)
        article.download()
        article.parse()
        return article.text

    @staticmethod
    def summarize_text(text: str, sentences_count: int = 5) -> str:
        parser = PlaintextParser.from_string(text, Tokenizer("english"))
        summarizer = LexRankSummarizer()
        summary = summarizer(parser.document, sentences_count)
        return "\n".join(str(sentence) for sentence in summary)

    @staticmethod
    def summarize_from_url(url: str, sentences_count: int = 5) -> str:
        try:
            full_text = Scrapper.get_article_text(url)
            return Scrapper.summarize_text(full_text, sentences_count)
        except Exception as e:
            return f"Error: {e}"

    def preprocess_text(text: str) -> str:
        text = text.replace("\n", " ").replace("\r", " ").strip()
        return text
