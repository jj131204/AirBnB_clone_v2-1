#!/usr/bin/python3
"""web_flask"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def index():
    """index"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """display “C ” followed by the value of the text variable"""
    return ('c ' + text.replace('_', ' '))


@app.route('/python')
@app.route('/python/<text>', strict_slashes=False)
def python_(text='is cool'):
    """" display “Python ”, followed by the value of the text variable"""
    return ('Python ' + text.replace('_', ' '))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
