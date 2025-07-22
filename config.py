from dotenv import load_dotenv
import os

load_dotenv()

TITLE = "Voice News Search Engine"
DESCRIPTION = "This app lets you search for news using your voice. Speak your query, and the app will transcribe it, search for relevant news, and read the results back to you!"
SERPER_API_KEY = os.getenv("SERPER_API_KEY")