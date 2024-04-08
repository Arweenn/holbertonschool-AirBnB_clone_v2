#!/usr/bin/python3
"""
Script that starts a Flask web app.
"""

from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def display_hello():
    return 'Hello HBNB!'


@app.route("/hbnb", strict_slashes=False)
def display_hbnb():
    return 'HBNB'


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    text = text.replace('_', ' ')
    return 'C' + text


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
