from pathlib import Path


def load_file(filename: Path) -> str:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        return content


def preprocessing(content: str) -> str:
    return (
        content.strip()
        .removeprefix("```markdown")
        .removeprefix("```md")
        .removeprefix("```json")
        .removeprefix("```")
        .removesuffix("```")
        .strip()
    )
