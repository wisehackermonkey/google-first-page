# by oran collins
# github.com/wisehackermonkey
# oranbusiness@gmail.com
# 20200404
# docs for Google-Search-API
# https://github.com/abenassi/Google-Search-API
from google import google 
# NOTE: on github/pypi "google" is called Google-Search-API
import json

def handle(search_query):
    """handle a request to the function
    Args:
        req (str): request body
    """
    result_json = []

    from google import google
    num_page = 1
    search_results = google.search(search_query, num_page)
    for result in search_results:
        # print(result.name)
        # print(f"        {result.description}")

        result_json.append( { "name": result.name, 
                              "link": result.link, 
                              "description": result.description})

    return result_json

# print(handle("hello world"))