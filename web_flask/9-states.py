#!/usr/bin/python3
"""This module defines a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
def states_list():
    """Displays an HTML page with a list of all States objects"""
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    for state in states:
        state.cities = sorted(state.cities, key=lambda city: city.name)
    return render_template('9-states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception=None):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states/<id>')
def states_id(id):
    """Displays an HTML page with a list of all States and Cities objects"""
    state = None
    for st in storage.all(State).values():
        if st.id == id:
            state = st
            break
    if state is not None:
        cities = sorted(state.cities, key=lambda city: city.name)
    else:
        cities = []
    return render_template('9-states.html', state=state, cities=cities)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
