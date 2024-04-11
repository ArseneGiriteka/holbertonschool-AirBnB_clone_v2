#!/usr/bin/python3
"""
This module takes cares of to routes
"""


from flask import Flask


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
