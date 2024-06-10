#!/usr/bin/python3
"""
Module define the rout URL
"""


from flask import Flask, render_template
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


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is cool"):
    """Return C + text given"""
    return "Python " + text.replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def n_route(n):
    """Return n +is a number if it's a number"""
    if isinstance(n, int):
        return str(n) + " is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def n_template_route(n):
    """Return a template"""
    if isinstance(n, int):
        return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def var_num_even_odd(n):
        """function to display even or odd number"""
        return render_template("6-number_odd_or_even.html", n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
