def keyword_movie_search_titles(searched_query: str, movies_data: dict, case_insensitive=False) -> list[dict]:

    results = []

    if not searched_query:
        print("NO SEARCH QUERY PROVIDED")
        return results
    
    if case_insensitive:
        return [m for m in movies_data['movies'] if searched_query.lower() in m['title'].lower()]

    return [m for m in movies_data['movies'] if searched_query in m['title']]