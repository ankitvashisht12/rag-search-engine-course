#!/usr/bin/env python3

import argparse

from utils.load_movies_data import load_movies_data
from utils.return_keyword_search_results import keyword_movie_search_titles
from utils.query_tokenizer import query_tokenizer
from tf_idf.inverted_index import InvertedIndex

def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    build_parser = subparsers.add_parser("build", help="Build the inverted index and save it to disk")

    args = parser.parse_args()

    inverted_index = InvertedIndex()

    match args.command:
        case "search":
            searched_query = args.query

            # movies_data = load_movies_data()
            # search_results = keyword_movie_search_titles(searched_query, movies_data, True)[:5]

            # print(f"Searching for: {searched_query}")
            # # print("Result:", search_results)
            # for movie in search_results:
            #     print(f"{movie['id']}. {movie['title']}")

            inverted_index.load()

            doc_ids_results = []
            for token in query_tokenizer(searched_query):
                doc_ids = inverted_index.get_documents(token)
                doc_ids_results.extend(doc_ids)
                doc_ids_results = list(set(doc_ids_results))
                if len(doc_ids_results) >= 5:
                    break
            
            doc_ids_results = sorted(doc_ids_results)[:5]

            for doc_id in doc_ids_results:
                movie = inverted_index.docmap[doc_id]
                print(f"{doc_id}. {movie['title']}")




        case "build":
            # inverted_index = InvertedIndex()
            inverted_index.build()

            # doc_ids = inverted_index.get_documents("merida")
            # print(f"First document for token 'merida' = {doc_ids[0]}")

            inverted_index.save()


        case _:
            parser.print_help()

if __name__ == "__main__":
    main()