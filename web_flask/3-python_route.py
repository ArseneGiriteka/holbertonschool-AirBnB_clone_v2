#!/usr/bin/python3
"""
This module takes cares of three routes
"""


from flask import Flask
from markupsafe import escape


app = Flask('__name__')


@app.route('/', strict_slashes=False)
def hello_HBNB():
    """
    print Hello HBNB! by returning it
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """
    print HBNB! by returning it
    """
    return 'HBNB'


@app.route('/c/<word_text>', strict_slashes=False)
def display_C(word_text):
    """
    this function displays C
    """
    return 'C ' + escape(word_text.replace('_', ' '))


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def display_python(text='is cool'):
    """
    this is a about python and not c
    """
    return 'Python ' + escape(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
