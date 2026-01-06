from .query_tokenizer import query_tokenizer


def matching_query_and_title(query: str, title: str) -> bool:

    if not query or not title:
        return False

    query_tokens = query_tokenizer(query)

    for token in query_tokens:
        if token in title:
            return True

    return False