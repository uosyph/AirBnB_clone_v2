#!/usr/bin/python3
"""Starts a Flask web application listening on 0.0.0.0, port 5000"""

from flask import Flask
from flask import render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/states", defaults={"id": None})
@app.route("/states/<id>")
def states_id(id):
    """/states: display a HTML page: (inside the tag BODY)"""
    states = storage.all(State)
    if id:
        id = f"State.{id}"
    return render_template("9-states.html", states=states, id=id)


@app.teardown_appcontext
def close_storage(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
