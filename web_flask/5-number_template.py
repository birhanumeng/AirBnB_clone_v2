#!/usr/bin/python3
""" Starts a Flask web application"""

from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """Displays Hello HBNB!"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displays HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def describ_c(text):
    """Display C followed by the values the text varaible"""
    return 'C %s' % text.replace('_', ' ')


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def describe_python(text='is cool'):
    """Display 'Python' followed by the values the text varaible"""
    return 'Python %s' % text.replace('_', ' ')


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Displays 'n is a nmuber' n is a var substituted by value"""
    return '%d is a number' % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def numbers_template(n):
    """Dispalys a HTML page only if n is an integer"""
    return render_template('5-number.html', n=n)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
