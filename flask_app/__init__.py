from flask import Flask, jsonify, request, json

import requests
import logging

from redis import StrictRedis,Redis



app = Flask(__name__)
config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "redis", # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300,
	"CACHE_HOST":'redis',
	"CACHE_PORT":6379,
	"CACHE_PASSWORD":""
}

app.config.from_mapping(config)


#redis = Redis(host='redis',port=6379)
# cache = Redis(host='redis', port=6379)

def register_blueprint(app):
    from .frontend import frontend
    app.register_blueprint(frontend)

register_blueprint(app)

@app.route('/check')
def check():
	return jsonify({'ceks':'cek'})
