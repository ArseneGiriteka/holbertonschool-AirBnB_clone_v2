#!/usr/bin/python3
"""This module defines a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """Displays an HTML page with a list of all States objects"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('7-states_list.html', states=states)


@app.route('/cities_by_states')
def cities_by_states():
    """Displays an HTML page with a list of all States and Cities objects"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    cities = storage.all(City).values()
    cities = sorted(cities, key=lambda city: city.name)
    return render_template('8-cities_by_states.html', states=states, cities=cities)


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
