from .remove_punctuation import remove_punctuation
from .remove_stopwords import remove_stopwords
from .stemmer import stem_it
from .query_tokenizer import query_tokenizer


        # if case_insensitive:
        #     searched_query = searched_query.lower()
        #     movie_title = movie_title.lower()
        
        # if should_remove_punctuation:
        #     searched_query = remove_punctuation(searched_query)
        #     movie_title = remove_punctuation(movie_title)

        # if should_remove_stopwords:
        #     searched_query, movie_title = remove_stopwords(searched_query, movie_title)

        # if should_stem:
        #     searched_query = stem_it(searched_query)

        # if matching_query_and_title(searched_query, movie_title):
        #     results.append(movie)

def clean_query_and_return_tokens(query: str) -> list[str]:
        if not query:
                return []

        query = query.lower()
        query = remove_punctuation(query)
        query, _ = remove_stopwords(query, "")
        query = stem_it(query)

        tokens = query_tokenizer(query)
        return tokens

