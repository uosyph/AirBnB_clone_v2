#!/usr/bin/python3
"""Starts a Flask web application listening on 0.0.0.0, port 5000"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    """/: display 'Hello HBNB!'"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """/hbnb: display “HBNB”"""
    return "HBNB"


@app.route("/c/<string:text>")
def ctext(text):
    """/c/<text>: display 'C ' followed by the value of the text variable
    (replaceing '_' with a space)"""
    text = text.replace("_", " ")
    return f"C {text}"


@app.route("/python/", defaults={"text": "is cool"})
@app.route("/python/<string:text>")
def pythontext(text="is cool"):
    """/python/<text>: display “Python ”, followed by the value of
    the text variable (replaceing '_' with a space)
    Default value: “is cool”"""
    text = text.replace("_", " ")
    return f"Python {text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
