#!/usr/bin/env python

from flask import Flask

from .versions import versions

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World..."

if __name__ == "__main__":
    app.run()