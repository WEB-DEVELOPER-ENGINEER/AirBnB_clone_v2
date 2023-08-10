#!/usr/bin/python3
"""Starts a Flask web app listening on 0.0.0.0, port 5000.
Routes:
    /hbnb_filters: HBnB HTML filters page."""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
app = Flask(__name__)


@app.teardown_appcontext
def close(self):
    """Closes session"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_route():
    """/hbnb_filters route"""
    s = list(storage.all(State).values())
    c = list(storage.all(City).values())
    a = list(storage.all(Amenity).values())
    c.sort(key=lambda x: x.name)
    s.sort(key=lambda x: x.name)
    a.sort(key=lambda x: x.name)
    return render_template('10-hbnb_filters.html', state=s, city=c, amenity=a)


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0')
