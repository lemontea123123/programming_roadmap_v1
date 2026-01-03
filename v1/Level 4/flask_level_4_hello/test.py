"""
Docstring for test
Testing Flask

"""

from flask import Flask

last_id = 3

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

def add_movie(movie_name,movie_content):
    global last_id

    new_id = last_id + 1
    last_id = new_id
    new_movie_dict = {
        "id": new_id ,
        "title":movie_name,
        "content":movie_content
    }
    list_movie.append(new_movie_dict)

def del_movie(movie_id):
    target_index = -1

    list_movie_indexes = enumerate(list_movie,start=0)
    for index , movie_dict in list_movie_indexes:
        current_movie_id = movie_dict["id"]
        if current_movie_id == movie_id :
            target_index = index
            break
    
    if(target_index == -1):
        print("Movie ID Out Of Range")
        return
    
    list_movie.pop(target_index)
    




print("list movie:\n",list_movie,"\nLast ID:",last_id,"\n")
add_movie("Fatman","Film tentang Fatman")
print("list movie:\n",list_movie,"\nLast ID:",last_id,"\n")

del_movie(1)
del_movie(2)