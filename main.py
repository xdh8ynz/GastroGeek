import logging
import os

from dotenv import load_dotenv
from openai import OpenAI

from constants import *
from core import generate_recipe

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

if __name__ == "__main__":
    logger.info("Приложение запущено!")

    load_dotenv()
    ai_api_key = os.getenv("AI_API_KEY")
    ai_base_url = os.getenv("AI_BASE_URL")

    if not ai_api_key or not ai_base_url:
        logger.error(
            "Ошибка! Для работы приложения обязательно задайте "
            "API-ключ и endpoint модели в .env файле"
        )
        raise SystemExit()

    client = OpenAI(
        api_key=ai_api_key,
        base_url=ai_base_url,
        timeout=TIMEOUT,
        max_retries=MAX_RETRIES,
    )

    recipe = generate_recipe(
        ingredients="Творог 9%, яблоки, изюм, вода, шоколад, "
        "кабачковая икра, хлебцы, кукуруза, греча, макароны",
        client=client,
    )
    logger.info(recipe)
