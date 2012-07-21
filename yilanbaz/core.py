#!/usr/bin/env python

import requests
from flask import Flask, Response

from .versions import versions

DIST_BASE = 'http://envy-versions.s3.amazonaws.com/'

app = Flask(__name__)


def fetch_dist(dist):
    url = DIST_BASE + dist
    r = requests.get(url)
    r.raise_for_status()

    return r.iter_content()

@app.route("/")
def hello():
    return "Hello World..."


@app.route('/dists/<dist>')
def get_dist(dist):
    g = fetch_dist(dist)

    return Response(g)



if __name__ == "__main__":
    app.run()