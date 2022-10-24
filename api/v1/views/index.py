#!/usr/bin/python3
""" index """
from flask import jsonify
from api.v1.views import app_views
from models import storage
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User

@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
	""" API status """
	return jsonify({"status": "OK"})

@app_views.route('/stats', methods=["GET"], strict_slashes=False)
def stats():
	""" Retrieve number of each object """
	classes = [Amenity, City, Place, Review, State, ]
	names = ["amenities", "cities", "places", "reviews", "states", "users"]
	obj_count = {}

	for i in range(len(classes)):
		obj_count[names[i]] = storage.count(classes[i])

	return jsonify(obj_count)