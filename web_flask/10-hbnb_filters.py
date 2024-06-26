#!/usr/bin/python3
"""
Script that starts a Flask web app.
"""

from models import storage
from flask import render_template, Flask
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def remove_sqlsession(exception=None):
    """A method that removes SQL Session"""
    storage.close()


@app.route("/hbnb_filters", strict_slashes=False)
def hbnb_filters():
    """Display HBNB filters"""
    list_states = storage.all(State)
    list_amenity = storage.all(Amenity)
    return render_template("10-hbnb_filters.html", states=list_states,
                           amenities=list_amenity)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
