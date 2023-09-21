#!/usr/bin/python3
"""Starts a Flask web application listening on 0.0.0.0, port 5000"""

from flask import Flask

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/")
def index():
    """Route index"""
    return "Hello HBNB!"


@app.route("/hbnb")
def hbnb():
    """Route index"""
    return "HBNB"


@app.route("/c/<string:text>")
def ctext(text):
    """Route index"""
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
