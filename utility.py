def load_file(filename: str) -> str:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        return content
