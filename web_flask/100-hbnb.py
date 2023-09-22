#!/usr/bin/python3
"""Starts a Flask web application listening on 0.0.0.0, port 5000"""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.user import User

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route("/hbnb")
def hbnb_advance_display():
    """/hbnb_filters: display a HTML page: (inside the tag BODY)"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    places = storage.all(Place).values()
    users = storage.all(User)
    new_dict = {}
    for key, value in users.items():
        new_dict[key.split(".")[-1]] = value
    return render_template(
        "100-hbnb.html",
        states=states,
        amenities=amenities,
        places=places,
        users=new_dict,
    )


@app.teardown_appcontext
def use_teardown(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
