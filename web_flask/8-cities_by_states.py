#!/usr/bin/python3
"""
Starts a flask application.
"""


from flask import Flask, escape, render_template
from models import storage, State


app = Flask(__name__)


@app.teardown_appcontext
def remove_session(self):
    """
    Remove the current SQLAlchemy Session after each request.
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def get_cities_by_states_list():
    """
    Return cities by states list HTML template.
    """
    states = []
    for k, v in (storage.all(State)).items():
        states.append(v)
    r = render_template(
        '8-cities_by_states.html',
        states=states
    )
    return r


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
