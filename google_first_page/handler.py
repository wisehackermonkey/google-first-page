# gets the url's and text of the first page of google givin search string
# by oran collins
# github.com/wisehackermonkey
# oranbusiness@gmail.com
# 20200404
# docs for Google-Search-API
# https://github.com/abenassi/Google-Search-API
from google import google 
# https://stackoverflow.com/questions/38635419/searching-in-google-with-python
# NOTE: on github/pypi "google" is called Google-Search-API
import json

def handle(search_query):
    """handle a request to the function
    Args:
        req (str): request body
    """
    #holds the contents of the page
    result_json = []

    from google import google
    num_page = 1 #only get the first page of google
    search_results = google.search(search_query, num_page)
    
    for result in search_results:
        # add the contents of the first page of google to a json array
        # containing the name of the link, the link itself, and the text from the page
        # 
        # example data:
        # (name) "Hello, World!" program - Wikipediaen.wikipedia.org › wiki › "Hello,_World!"_program
        # (description) A "Hello, World!" program generally is a computer program that outputs or displays the message "Hello, World!". Such a program is very simple in most programming languages, and is often used to illustrate the basic syntax of a programming language. It is often the first program written by people learning to code.
        # (link) https://en.wikipedia.org/wiki/%22Hello,_World!%22_program
        result_json.append( { "name": result.name, 
                              "link": result.link, 
                              "description": result.description})

    return repr(result_json)

# if running locally uncommend this code and run
# >python ./google_first_page/handler.py
# print(handle("hello world"))