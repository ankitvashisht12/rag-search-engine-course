from nltk.stem import PorterStemmer
from .query_tokenizer import query_tokenizer

stemmer = PorterStemmer()

def stem_it(searched_query: str) -> str:

    query_tokens = query_tokenizer(searched_query)

    stemmed_query_tokens = []

    for token in query_tokens:
        stemmed_token = stemmer.stem(token)
        stemmed_query_tokens.append(stemmed_token)

    return " ".join(stemmed_query_tokens)
