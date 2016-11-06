from flask import jsonify, abort, request
from . import app

from .models import Location

@app.route('/')
def get_locations():
	return Location.get_all()

@app.route('/latest')
def latest_location():
	return Location.get_latest()
