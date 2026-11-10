from pathlib import Path

import openai
from openai import OpenAI
from openai.types.chat import (
    ChatCompletionSystemMessageParam,
    ChatCompletionUserMessageParam,
)

from utility import load_file, preprocessing

TOP_PROBABILITY = 0.7
TEMPERATURE = 0.8


def generate_recipe(
    ingredients: str,
    client: OpenAI,
) -> str:
    parent_path = Path(__file__).resolve().parent
    system_prompt = load_file(parent_path / "system_prompt.xml")
    user_prompt = load_file(parent_path / "user_prompt.xml").format(
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
            model="google/gemma-3-4b-it",
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
