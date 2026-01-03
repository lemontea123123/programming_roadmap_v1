"""
Docstring for test
Testing Flask

"""

from flask import Flask

list_movie = [
    {
        "id":1,
        "title":"Batman",
        "content":"Film Batman"
    },
    {
        "id":2,
        "title":"Fatman",
        "content":"Film tentang Fatman"
    },
    {
        "id":3,
        "title":"Catman",
        "content":"Film tentang Catman"
    }
]

list_kosong = []

def get_last_index(list):
    last_index = len(list)-1

    if(last_index > 0):
        last_movie_id = list[last_index]["id"]
        return last_movie_id
    else:
        return 0

print(get_last_index(list_movie))