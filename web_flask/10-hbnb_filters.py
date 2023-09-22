#!/usr/bin/python3
"""Starts a Flask web application listening on 0.0.0.0, port 5000"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/hbnb_filters")
def hbnb_filters():
    """/hbnb_filters: display a HTML page: (inside the tag BODY)"""
    states = storage.all("State")
    am = storage.all("Amenity")
    return render_template("10-hbnb_filters.html", states=states, amenities=am)


@app.teardown_appcontext
def use_teardown(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
