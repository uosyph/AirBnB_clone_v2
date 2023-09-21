#!/usr/bin/python3
"""Starts a Flask web application listening on 0.0.0.0, port 5000"""

from flask import Flask, render_template

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


@app.route("/python/", defaults={"text": "is cool"})
@app.route("/python/<string:text>")
def pythontext(text="is cool"):
    """Route index"""
    text = text.replace("_", " ")
    return "Python {}".format(text)


@app.route("/number/<int:num>")
def number(num):
    """Route index"""
    return "{} is a number".format(num)


@app.route("/number_template/<int:num>")
def number_template(num):
    """Route index"""
    return render_template("5-number.html", value=num)


@app.route("/number_odd_or_even/<int:num>")
def odd_or_even(num):
    """Route index"""
    if num & 1:
        data = "{} is odd".format(num)
    else:
        data = "{} is even".format(num)
    return render_template("6-number_odd_or_even.html", value=data)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
