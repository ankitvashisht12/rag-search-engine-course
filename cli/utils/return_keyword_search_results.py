def keyword_movie_search_titles(searched_query, movies_data):

    results = []

    if not searched_query:
        print("NO SEARCH QUERY PROVIDED")
        return results

    return [m for m in movies_data['movies'] if searched_query in m['title']]