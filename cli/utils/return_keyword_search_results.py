from .remove_punctuation import remove_punctuation

def keyword_movie_search_titles(searched_query: str, movies_data: dict, case_insensitive=False, should_remove_punctuation=True) -> list[dict]:

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

        if searched_query in movie_title:
            results.append(movie)

    return results