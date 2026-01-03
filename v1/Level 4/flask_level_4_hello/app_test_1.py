"""
Docstring for app_test_1
    Ini saya lakukan di Folder flask_level_4_hello di file test.py

5.	Template HTML dengan Flask
o	Pindahkan HTML dari form.html ke folder templates/index.html.geeksforgeeks
o	Modifikasi route / supaya render_template('index.html').
6.	Route GET & POST
o	Buat route /submit yang menerima POST dari form.flask.palletsprojects
o	Ambil data dari request.form['judul'] dan request.form['isi'], lalu print di terminal dan tampilkan kembali di halaman (misal pakai template result.html).

"""

from flask import Flask , render_template , request
from werkzeug.exceptions import BadRequestKeyError
from flask import jsonify
from flask import redirect
from flask import url_for

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
        return -1
    
    list_movie.pop(target_index)
    return target_index
    
app = Flask(__name__)

@app.route("/")
def show_form_index_html():
    return render_template("index.html",list_movie=list_movie)

@app.route("/add",methods=["GET","POST"])
def add_refresh_index_html():
    try :
        title = request.form["title"]
        content = request.form["content"]
    except BadRequestKeyError:
        return render_template("index.html",error="Please Fill In Information",list_movie=list_movie)
    
    add_movie(title,content)

    return render_template("index.html",list_movie=list_movie)

@app.route("/submit",methods=["GET","POST"])
def show_result_result_html():
    try :
        title = request.form["title"]
        content = request.form["content"]
    except BadRequestKeyError:
        return render_template("index.html",error="Please Fill In Information")

    return render_template("result.html",title=title,content=content)

@app.route("/delete/<int:id>")
def delete_and_refresh_index_html(id):
    del_movie(id)
    #return render_template("index.html",list_movie=list_movie)
    return redirect(url_for("show_form_index_html"))



@app.route("/api/notes",methods=["GET"])
def return_notes_list():
    return jsonify(list_movie)

@app.route("/api/add_note",methods=["POST"])
def add_note():
    note_obj = request.get_json()

    print("Received JSON:\n",note_obj)

    title = note_obj["title"]
    content = note_obj["content"]

    add_movie(title,content)

    return {
        "status":"ok"
    }

@app.route("/api/notes/<int:id>",methods=["DELETE"])
def api_delete_note(id):
    if(del_movie(id) != -1 ):
        response = {
            "status":"deleted"
        }
    else:
        response = {
            "status":"ID Not Found"
        }

    return response

if(__name__ == "__main__"):
    app.run(debug=True)

