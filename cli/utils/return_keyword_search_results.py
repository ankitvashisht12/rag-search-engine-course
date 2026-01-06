from .remove_punctuation import remove_punctuation
from .matching_query_and_title import matching_query_and_title
from .remove_stopwords import remove_stopwords

def keyword_movie_search_titles(searched_query: str, movies_data: dict, case_insensitive=False, should_remove_punctuation=True, should_remove_stopwords=True) -> list[dict]:

    results = []

    if not searched_query:
        print("NO SEARCH QUERY PROVIDED")
        return results

    movies = movies_data.get("movies", [])
    for movie in movies:
        movie_title = movie["title"]

        if case_insensitive:
            searched_query = searched_query.lower()
            movie_title = movie_title.lower()
        
        if should_remove_punctuation:
            searched_query = remove_punctuation(searched_query)
            movie_title = remove_punctuation(movie_title)

        if should_remove_stopwords:
            searched_query, movie_title = remove_stopwords(searched_query, movie_title)

        if matching_query_and_title(searched_query, movie_title):
            results.append(movie)

    return results