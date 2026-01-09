from collections import Counter
import pickle 
from pathlib import Path
import os
from utils.query_tokenizer import query_tokenizer
from utils.load_movies_data import load_movies_data
from utils.clean_query_and_return_tokens import clean_query_and_return_tokens

BASE_PATH = Path(__file__).resolve().parents[2]
CACHE_DIR = BASE_PATH / "cache"
INDEX_CACHE_PATH = os.path.join(CACHE_DIR, "index.pkl")
DOC_MAP_CACHE_PATH = os.path.join(CACHE_DIR, "docmap.pkl")
TERM_FREQUENCIES_CACHE_PATH = os.path.join(CACHE_DIR, "term_frequencies.pkl")
class InvertedIndex:
    index: dict[str, list[int]]
    docmap: dict[int, dict[str, str]]
    term_frequencies: dict[int, Counter] # { doc_id: counter dict of each term in that document }

    def __init__(self) -> None:
        self.index = {}
        self.docmap = {}
        self.term_frequencies = {}

    def __add_document(self, doc_id: int, text: str) -> None:
        tokens = clean_query_and_return_tokens(text)

        for token in tokens:
            if token not in self.index:
                self.index[token] = []
            self.index[token].append(doc_id)

            # building term frequencies
            if doc_id not in self.term_frequencies:
                self.term_frequencies[doc_id] = Counter()

            self.term_frequencies[doc_id][token] += 1

    def get_documents(self, term: str) -> list[int]:
        if term.lower() not in self.index:
            return []
        doc_ids = sorted(self.index[term.lower()])
        return doc_ids

    def get_tf(self, doc_id: int, term: str) -> int:
        tokens = clean_query_and_return_tokens(term)

        if len(tokens) > 1:
            raise Exception("TF can only be calculated for a single term")

        return self.term_frequencies.get(doc_id, Counter()).get(tokens[0], 0)


    def build(self) -> None:
        movies_json = load_movies_data()

        movies = movies_json.get("movies", [])

        for movie in movies:
            text = f"{movie['title']} {movie['description']}"

            # building index
            self.__add_document(movie['id'], text)

            # building docmap
            self.docmap[movie['id']] = movie


    def load(self) -> None:
        try:
            with open(INDEX_CACHE_PATH, 'rb') as file:
                self.index = pickle.load(file)
            with open(DOC_MAP_CACHE_PATH, 'rb') as file:
                self.docmap = pickle.load(file)
            with open(TERM_FREQUENCIES_CACHE_PATH, 'rb') as file:
                self.term_frequencies = pickle.load(file)
        except FileNotFoundError:
            print("Error: Files don't exist")

    

    def save(self) -> None:

        os.makedirs(CACHE_DIR, exist_ok=True)

        with open(INDEX_CACHE_PATH, 'wb') as file:
            pickle.dump(self.index, file)

        with open(DOC_MAP_CACHE_PATH, 'wb') as file:
            pickle.dump(self.docmap, file)
        
        with open(TERM_FREQUENCIES_CACHE_PATH, 'wb') as file:
            pickle.dump(self.term_frequencies, file)