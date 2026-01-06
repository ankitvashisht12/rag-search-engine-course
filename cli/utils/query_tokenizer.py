def query_tokenizer(query: str) -> list[str]:
    """ This will create word tokens from a given query string."""

    if not query:
        return []

    # Split the query into words based on whitespace
    tokens = query.split()

    tokens = [t for t in tokens if t != ""]

    return tokens
