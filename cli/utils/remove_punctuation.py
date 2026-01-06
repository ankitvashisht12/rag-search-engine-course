from string import punctuation
def remove_punctuation(query: str) -> str:
    if not query:
        return query

    return query.translate(str.maketrans("", "", punctuation))