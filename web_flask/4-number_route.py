#!/usr/bin/python3
"""
   Module define the rout URL
"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """root Method"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """Return C + text given"""
    return "C " + text.replace("_", " ")


@app.route('/python/<text>', strict_slashes=False)
def python_route(text default: "is cool"):
    """Return C + text given"""
    return "Python " + text.replace("_", " ")


@app.route('/number/<n>', strict_slashes=False)
def n_route(n):
    """Return n +is a number if it's a number"""
    if isinstance(n, int):
        return n + " is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
