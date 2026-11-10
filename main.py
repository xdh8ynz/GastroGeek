import os

from dotenv import load_dotenv
from openai import OpenAI
from openai.types.chat import ChatCompletionUserMessageParam

if __name__ == "__main__":
    load_dotenv()

    client = OpenAI(api_key=os.getenv("AI_API_KEY"), base_url=os.getenv("AI_BASE_URL"))

    user_message = ChatCompletionUserMessageParam(
        role="user", content="Каковы основные идеи философии Шопенгауэра?"
    )

    response = client.chat.completions.create(
        model="google/gemma-3-4b-it",
        messages=[user_message],
    )

    print(response.choices[0].message.content)
