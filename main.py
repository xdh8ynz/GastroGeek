import logging
import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

from web import routes

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

app = FastAPI()
app.include_router(routes.router)

if __name__ == "__main__":
    logger.info("Приложение запущено!")

    load_dotenv()
    ai_api_key = os.getenv("AI_API_KEY")
    ai_base_url = os.getenv("AI_BASE_URL")

    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
