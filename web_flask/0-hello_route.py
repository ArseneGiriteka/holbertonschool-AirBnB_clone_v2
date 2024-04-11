#!/usr/bin/python3
"""
New Module
that print a simple message
"""


from flask import Flask

"""Creating new app"""
app = Flask(__name__)


"""routing hello"""


@app.route('/', strict_slashes=False)
def hello():
    """
    Print Hello HBNB! by returning it
    """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
