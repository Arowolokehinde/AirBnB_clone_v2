#!/usr/bin/python3

"""Script that starts a Flask web application"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """print to the web"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """ Displays HNBN"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def display_c_text(text):
    """ displays C followed by the value of the text variable"""
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/')
@app.route('/python/<text>')
def display_python_text(text='is cool'):
    """ """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def display_number(n):
    return f'{n} is a number'


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_number_template(n):
    """Displays an HTML page only if <n> is an integer."""
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
