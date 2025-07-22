from dotenv import load_dotenv
import os

load_dotenv()

class AppConfig:
    APP = {
        "ICON": "assets/images/hcmus_logo.png"
    },
    APP_HEADER = {
        "TITLE": "Trợ Lý Tìm Kiếm Tin Tức Bằng Giọng Nói",
        "DESCRIPTION": "Tìm kiếm và khám phá tin tức dễ dàng qua giọng nói. Chỉ cần nói điều bạn quan tâm, hệ thống sẽ tìm các bài viết phù hợp và đọc nội dung cho bạn nghe bằng giọng nói tự nhiên.",
    }
    SERPER_API_KEY = os.getenv("SERPER_API_KEY")
