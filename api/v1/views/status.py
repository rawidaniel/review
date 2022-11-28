#!/usr/bin/python3
'''
    RESTful API for status and total number of each class object
'''
from api.v1.views import all_views
from flask import jsonify
from models import classes, storage


@all_views.route("/status")
def status():
    """Return the status of the API OK"""
    return jsonify({"status": "OK"})


@all_views.route("/stats")
def stats():
    """Return the count of each class"""
    new_dict = {}
    for cls in classes:
        if cls != 'BaseModel':
            new_dict[cls] = storage.count(cls)
    return jsonify(new_dict)
