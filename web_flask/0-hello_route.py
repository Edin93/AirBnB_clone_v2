#!/usr/bin/python3
"""
Starts a flask application.
"""


from flask import Flask


app = Flask(__name__.split('.')[0])
@app.route('/', strict_slashes=False)
def index():
    """
    Returns a welcoming message.
    """
    return "Hello HBNB!"
app.run(host='0.0.0.0', port=5000)
