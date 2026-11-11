import json

from fastapi import APIRouter, Request, status
from starlette.responses import HTMLResponse, JSONResponse
from starlette.templating import Jinja2Templates

import ai.recipe_generator
from ai.ai_client import client
from core.logger import logger
from core.utility import preprocessing

templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def show_root_page(request: Request):
    return templates.TemplateResponse(request, "index.html")


# TODO: сделать асинхронной
# TODO: добавить генерацию ккал
# TODO: добавить валидацию JSON
# TODO: добавить индикатор загрузки
# TODO: добавить pydantic
@router.get("/generate", response_class=JSONResponse)
def generate_recipe(ingredients: str):
    recipe = ai.recipe_generator.generate_recipe(ingredients, client)

    try:
        recipe_json = json.loads(preprocessing(recipe))
    except json.JSONDecodeError as exception:
        logger.warn("Некорректный JSON: ", exception.msg)
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"error": exception.msg},
        )

    return JSONResponse(content=recipe_json)
