#!/usr/bin/python3
"""Starts a Flask web app listening on 0.0.0.0, port 5000.
Routes:
    /states_list: HTML page with a list of all State objects in DBStorage.
"""
from models import storage
from flask import Flask
from models.state import State
from flask import render_template
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list():
    """Displays an HTML page with a list of all State objects in DBStorage.
    """
    states_list = list(storage.all(State).values())
    states_list.sort(key=lambda x: x.name)
    return render_template('7-states_list.html', states=states_list)


@app.teardown_appcontext
def close(self):
    """Closes session"""
    storage.close()

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
