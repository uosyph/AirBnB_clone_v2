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


@app.teardown_appcontext
def teardown(self):
    storage.close()


@app.route("/")
def index():
    """/: display 'Hello HBNB!'"""
    return "Hello HBNB!"


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


@app.route("/number/<int:num>")
def number(num):
    """/number/<n>: display a number only if n is an integer"""
    return f"{num} is a number"


@app.route("/number_template/<int:num>")
def number_template(num):
    """/number_template/<n>: display a HTML page only if n is an integer"""
    return render_template("5-number.html", value=num)


@app.route("/number_odd_or_even/<int:num>")
def odd_or_even(num):
    """/number_odd_or_even/<n>: display a HTML page only if n is an integer"""
    if num & 1:
        data = f"{num} is odd"
    else:
        data = f"{num} is even"
    return render_template("6-number_odd_or_even.html", value=data)


@app.route("/states_list")
def states_list():
    """/states_list: display a HTML page: (inside the tag BODY)"""
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


@app.route("/cities_by_states")
def cities_by_states_list():
    """/states: display a HTML page: (inside the tag BODY)
    /states/<id>: display a HTML page: (inside the tag BODY)"""
    states = storage.all(State).values()
    return render_template("8-cities_by_states.html", states=states)


@app.route("/states/", defaults={"id": None})
@app.route("/states/<id>")
def states_id(id):
    """/states: display a HTML page: (inside the tag BODY)"""
    in_list = False
    states = storage.all(State).values()
    for state in states:
        in_list = True
        if id == state.id:
            return render_template("9-states.html", states=state)
    if id is not None and in_list == True:
        return render_template("9-states.html", states=None)
    return render_template("9-states.html", states=states)


@app.route("/hbnb_filters")
def hbnb_filters():
    """/hbnb_filters: display a HTML page: (inside the tag BODY)"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template("10-hbnb_filters.html", states=states, amenities=amenities)


@app.route("/hbnb")
def hbnb_advance_display():
    """/hbnb: display a HTML page: (inside the tag BODY)"""
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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
