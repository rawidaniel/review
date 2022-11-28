#!/usr/bin/python3
"""
Initalize flask application for RESTful API
"""
from flask import Flask, make_response, jsonify
from os import getenv
from models import storage
from api.v1.views import all_views
from flask_cors import CORS

app = Flask(__name__)
app.register_blueprint(all_views)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.teardown_appcontext
def tear_down(self):
    '''close query after each session'''
    storage.close()


@app.errorhandler(404)
def not_found(error):
    """Return error json file"""
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == "__main__":
    app.run(debug=True, host=getenv('HBNB_API_HOST', '0.0.0.0'),
            port=int(getenv("HBNB_API_PORT", "5001")), threaded=True)
