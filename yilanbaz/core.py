#!/usr/bin/env python

import requests
from flask import Flask, redirect, jsonify

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

@app.route('/dists/<style>/<version>')
def release_info(style, version):
    return jsonify(dist=versions[style][version])

@app.route('/dists/<style>/<version>/download')
def redirect_to_version(style, version):
    v = versions[style][version]
    return redirect(DIST_BASE + '/dists/' + v['dist'])

if __name__ == "__main__":
    app.run()