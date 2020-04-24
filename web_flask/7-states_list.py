#!/usr/bin/python3
"""
Starts a flask application.
"""


from flask import Flask, escape, render_template
from models import storage, State
from collections import OrderedDict


app = Flask(__name__)


@app.teardown_appcontext
def remove_session(self):
    """
    Remove the current SQLAlchemy Session after each request.
    """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def get_states_list():
    """
    Return states list HTML template.
    """
    states_list = [v for k, v in (storage.all(State)).items()]
    r = render_template(
        '7-states_list.html',
        states_list=states_list
    )
    return r


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
