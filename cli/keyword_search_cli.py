#!/usr/bin/env python3

import argparse

from utils.query_tokenizer import query_tokenizer
from tf_idf.inverted_index import InvertedIndex

import math

def main() -> None:
    parser = argparse.ArgumentParser(description="Keyword Search CLI")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    search_parser = subparsers.add_parser("search", help="Search movies using BM25")
    search_parser.add_argument("query", type=str, help="Search query")

    build_parser = subparsers.add_parser("build", help="Build the inverted index and save it to disk")
    
    tf_parser = subparsers.add_parser("tf", help="Calculate the TF for a given term and document")
    tf_parser.add_argument("doc_id", type=int, help="Document ID to calculate TF for")
    tf_parser.add_argument("term", type=str, help="Term to calculate TF for")

    idf_parser = subparsers.add_parser("idf", help="Calculate the IDF for a given term")
    idf_parser.add_argument("term", type=str, help="Term to calculate IDF for")

    tfidf_parser = subparsers.add_parser("tfidf", help="Calculate the TF-IDF for a given term and document")
    tfidf_parser.add_argument("doc_id", type=int, help="Document ID to calculate TF-IDF for")
    tfidf_parser.add_argument("term", type=str, help="Term to calculate TF-IDF for")

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


        case "tf":
            doc_id = args.doc_id
            term = args.term

            inverted_index.load()
            tf = inverted_index.get_tf(doc_id, term)
            print(tf)

        case "idf":
            inverted_index.load()
            idf_value = inverted_index.get_idf(args.term)

            print(f"Inverse document frequency of '{args.term}': {idf_value:.2f}")

        case "tfidf":
            doc_id = args.doc_id
            term = args.term

            inverted_index.load()
            
            tf = inverted_index.get_tf(doc_id, term)
            idf = inverted_index.get_idf(term)

            tf_idf = tf * idf

            print(f"TF-IDF score of '{args.term}' in document '{args.doc_id}': {tf_idf:.2f}")

        case _:
            parser.print_help()

if __name__ == "__main__":
    main()