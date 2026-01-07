import pickle 
from pathlib import Path
import os
from utils.query_tokenizer import query_tokenizer
from utils.load_movies_data import load_movies_data

class InvertedIndex:
    index: dict[str, list[int]]
    docmap: dict[int, str]

    def __init__(self) -> None:
        self.index = {}
        self.docmap = {}

    def __add_document(self, doc_id: int, text: str) -> None:
        tokens = query_tokenizer(text)

        for token in tokens:
            if token.lower() not in self.index:
                self.index[token.lower()] = []
            self.index[token.lower()].append(doc_id)

    def get_documents(self, term: str) -> list[int]:
        doc_ids = sorted(self.index[term.lower()])
        return doc_ids



    def build(self) -> None:
        movies_json = load_movies_data()

        movies = movies_json.get("movies", [])

        for movie in movies:
            text = f"{movie['title']} {movie['description']}"
            self.__add_document(movie['id'], text)



    def save(self) -> None:
        BASE_PATH = Path(__file__).resolve().parents[2]
        CACHE_DIR = BASE_PATH / "cache"
        INDEX_CACHE_PATH = os.path.join(CACHE_DIR, "index.pkl")
        DOC_MAP_CACHE_PATH = os.path.join(CACHE_DIR, "docmap.pkl")

        os.makedirs(CACHE_DIR, exist_ok=True)

        with open(INDEX_CACHE_PATH, 'wb') as file:
            pickle.dump(self.index, file)

        with open(DOC_MAP_CACHE_PATH, 'wb') as file:
            pickle.dump(self.docmap, file)