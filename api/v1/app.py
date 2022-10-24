#!/usr/bin/python3
""" Flask App """
from os import environ
from models import storage
from api.v1.views import app_views
from flask import Flask, jsonify, make_response

app = Flask(__name__)
app.register_blueprint(app_views)

@app.teardown_appcontext
def close_db(error):
	""" close storage """
	storage.close()

@app.errorhandler(404)
def not_found(error):
	""" error 404 """
	return make_response(jsonify({"error": "Not found"}), 404)

if __name__ == "__main__":
	""" Main func """
	host = environ.get('HBNB_API_HOST')
	port = environ.get('HBNB_API_PORT')
	if not host:
		host = '0.0.0.0'
	if not port:
		port = '5000'
	app.run(host=host, port=port, threaded=True)