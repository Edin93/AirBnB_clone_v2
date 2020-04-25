#!/usr/bin/python3
"""
Module for rendering hbnb_filters page.
"""


from flask import Flask, render_template
from models import storage, State, Amenity


app = Flask(__name__)


@app.teardown_appcontext
def remove_session(self):
    """
    Remove the current SQLAlchemy Session after each request.
    """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def get_hbnb_filter():
    """
    Returns hbnb filers HTML template.
    """
    states = [v for k, v in storage.all(State).items()]
    amenities = [v for k, v in storage.all(Amenity).items()]
    r = render_template(
        '10-hbnb_filters.html',
        states=states,
        amenities=amenities
    )
    return r


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
