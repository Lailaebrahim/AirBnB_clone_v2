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


@app.route('/hbnb')
def hbnb():
    """return HBNB"""
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
