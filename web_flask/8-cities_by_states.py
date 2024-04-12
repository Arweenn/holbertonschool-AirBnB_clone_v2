#!/usr/bin/python3
"""
Script that starts a Flask web app.
"""

from flask import Flask, render_template
from models import storage
from models.state import State, City

app = Flask(__name__)


@app.teardown_appcontext
def close_stor(exception=None):
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    states = sorted(storage.all(State).values(), key=lambda x: x.name)
    cities = sorted(storage.all(City).values(), key=lambda x: x.name)
    return render_template(
        "8-cities_by_states.html", states=states, cities=cities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
