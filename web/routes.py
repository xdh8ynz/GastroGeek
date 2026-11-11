from fastapi import APIRouter, Request
from starlette.responses import HTMLResponse, JSONResponse
from starlette.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")
router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def show_root_page(request: Request):
    return templates.TemplateResponse(request, "index.html")


# TODO: сделать асинхронной
@router.get("/generate", response_class=JSONResponse)
def generate_recipe(ingredients: str):
    print(ingredients)
    return {
        "title": "Курица с рисом и овощами",
        "description": "Простое и вкусное блюдо, которое идеально подойдет для семейного ужина. Нежная курица в сочетании с рассыпчатым рисом и хрустящими овощами.",
        "time": "60 минут",
        "difficulty": "Легкий рецепт",
        "ingredients": [
            "Куриное филе - 500 г",
            "Рис - 300 г",
            "Лук репчатый - 2 шт",
            "Морковь - 2 шт",
            "Чеснок - 3 зубчика",
            "Специи по вкусу",
            "Растительное масло - 2 ст. л.",
            "Соль и перец - по вкусу",
        ],
        "steps": [
            "Нарежьте курицу кубиками среднего размера",
            "Отварите рис до готовности согласно инструкции на упаковке",
            "Обжарьте курицу на сковороде до золотистой корочки",
            "Добавьте нарезанный лук и морковь, тушите 10 минут",
            "Добавьте измельченный чеснок и специи",
            "Смешайте готовый рис с курицей и овощами",
            "Подавайте горячим, украсив свежей зеленью",
        ],
        "tip": "Для более насыщенного вкуса можно добавить немного соевого соуса или томатной пасты.",
    }
