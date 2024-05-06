#!/usr/bin/python3
"""Module define the rout URL"""
from flask import Flask

app = Flask(__name__, strict_slashes=False)

@app.route('/')
def hello_hbnb():
    """root Method"""
    return "Hello HBNB!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000
