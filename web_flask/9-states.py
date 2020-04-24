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


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def get_state_by_id(id=None):
    """
    Return cities by states list HTML template.
    """
    store = storage.all(State)
    if id is None:
        one_state = None
        states = [v for k, v in store.items()]
    else:
        k = "<class 'models.state.State'>." + str(id)
        one_state = store.get(k, None)
        states = []
    r = render_template(
        '9-states.html',
        states=states,
        one_state=one_state
    )
    return r


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
