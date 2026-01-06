import json
from pathlib import Path

def load_movies_data() -> dict:

    BASE_PATH = Path(__file__).resolve().parents[2]
    DATA_PATH = BASE_PATH / "data" / "movies.json"
    with open(DATA_PATH, "r", encoding="utf-8") as file:
        movies_data = json.load(file)

    return movies_data


