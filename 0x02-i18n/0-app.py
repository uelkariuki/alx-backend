#!/usr/bin/env python3

"""Flask app"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello():
	"""Hello method"""
	return render_template('0-index.html')
