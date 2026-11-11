import uvicorn
from fastapi import FastAPI

from core.logger import logger
from web import routes

app = FastAPI()
app.include_router(routes.router)

if __name__ == "__main__":
    logger.info("Приложение запущено!")
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
