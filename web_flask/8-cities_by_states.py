#!/usr/bin/python3
"""Starts a Flask web app listening on 0.0.0.0, port 5000.
Routes:
    /cities_by_states: HTML with a list of all states and related cities"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def state_cities_list():
    """/cities_by_states route"""
    c = list(storage.all(City).values())
    s = list(storage.all(State).values())
    return render_template('8-cities_by_states.html', cities=c, states=s)


@app.teardown_appcontext
def close(self):
    """Closes session"""
    storage.close()


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
