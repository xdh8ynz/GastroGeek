from functools import cache
from pathlib import Path

import openai
from openai import OpenAI
from openai.types.chat import (
    ChatCompletionSystemMessageParam,
    ChatCompletionUserMessageParam,
)

from constants import *
from utility import load_file, preprocessing

parent_path = Path(__file__).resolve().parent


@cache
def generate_recipe(
    ingredients: str,
    client: OpenAI,
) -> str:
    system_prompt = load_file(parent_path / SYSTEM_PROMPT_PATH)
    user_prompt = load_file(parent_path / USER_PROMPT_PATH).format(
        ingredients=ingredients,
    )

    system_message = ChatCompletionSystemMessageParam(
        role="system",
        content=system_prompt,
    )

    user_message = ChatCompletionUserMessageParam(
        role="user",
        content=user_prompt,
    )

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[system_message, user_message],
            temperature=TEMPERATURE,
            top_p=TOP_PROBABILITY,
        )
    except openai.APIError as exception:
        return f"Ошибка: {exception.message}! Не удалось сгенерировать рецепт"

    content = response.choices[0].message.content

    if not content:
        return "Модель вернула пустой ответ"
    else:
        return preprocessing(content)
