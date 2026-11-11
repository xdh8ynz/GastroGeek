import os

from dotenv import load_dotenv
from openai import OpenAI

from core.constants import MAX_RETRIES, TIMEOUT

load_dotenv()

client = OpenAI(
    api_key=os.getenv("AI_API_KEY"),
    base_url=os.getenv("AI_BASE_URL"),
    timeout=TIMEOUT,
    max_retries=MAX_RETRIES,
)
