from openai import OpenAI
from openai.types.chat import (
    ChatCompletionSystemMessageParam,
    ChatCompletionUserMessageParam,
)

from utility import load_file

TOP_PROBABILITY = 0.7
TEMPERATURE = 0.8


def generate_recipe(
    ingredients: str,
    client: OpenAI,
) -> str:
    system_prompt = load_file("system_prompt.xml")
    user_prompt = load_file("user_prompt.xml").format(
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

    response = client.chat.completions.create(
        model="google/gemma-3-4b-it",
        messages=[system_message, user_message],
        temperature=TEMPERATURE,
        top_p=TOP_PROBABILITY,
    )

    return response.choices[0].message.content
