#!/usr/bin/env python3

import argparse

from utils.load_movies_data import load_movies_data
from utils.return_keyword_search_results import keyword_movie_search_titles

def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    args = parser.parse_args()

    match args.command:
        case "search":
            searched_query = args.query

            movies_data = load_movies_data()
            search_results = keyword_movie_search_titles(searched_query, movies_data, True)[:5]

            print(f"Searching for: {searched_query}")
            for movie in search_results:
                print(f"{movie['id']}. {movie['title']}")

        case _:
            parser.print_help()

if __name__ == "__main__":
    main()