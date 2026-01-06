from pathlib import Path
from .query_tokenizer import query_tokenizer

BASE_PATH = Path(__file__).resolve().parents[2]
STOPWORD_FILE_PATH = BASE_PATH / "data" / "stopwords.txt"

def remove_stopwords(query: str, title: str):
    if not query or not title:
        return query, title

    with open(STOPWORD_FILE_PATH, "r", encoding="utf-8") as file:
        stopwords =  file.read().splitlines()

    # remove stopwords from query and title
    query_tokens = query_tokenizer(query)
    title_tokens = query_tokenizer(title)
    for token in query_tokens:
        if token in stopwords:
            query_tokens.remove(token)
    
    for token in title_tokens:
        if token in stopwords:
            title_tokens.remove(token)

    return " ".join(query_tokens), " ".join(title_tokens)