import os

from dotenv import load_dotenv
from openai import OpenAI

from core import generate_recipe

if __name__ == "__main__":
    load_dotenv()
    client = OpenAI(api_key=os.getenv("AI_API_KEY"), base_url=os.getenv("AI_BASE_URL"))

    recipe = generate_recipe(
        ingredients="Творог 9%, яблоки, изюм, вода, шоколад, "
        "кабачковая икра, хлебцы, кукуруза, греча, макароны",
        client=client,
    )
    print(recipe)
