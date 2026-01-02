"""
Docstring for test
Testing Flask

"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_web():
    return "<h1>Hello , Web!</h1>"

if(__name__=="__main__"):
    app.run(debug=False)

    