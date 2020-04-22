#!/usr/bin/python3
"""
Starts a flask application.
"""


from flask import Flask, escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """
    Returns a welcoming message.
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def get_hbnb_page():
    """
    Returns /hbnb content.
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def get_c_page(text):
    """
    Return /c/<text> content.
    """
    return 'C %s' % text.replace('_', ' ')


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def get_python_page(text):
    """
    Return /python/(<text>) content.
    """
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def get_number_page(n):
    """
    Return if passed parameter a number or not.
    """
    return "{} is a number".format(n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
