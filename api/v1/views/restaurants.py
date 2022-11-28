#!/usr/bin/python3
'''
    RESTful API for class Restaurant
'''
from api.v1.views import all_views
from models import storage
from flask import jsonify, abort, request
from models.restaurant import Restaurant


@all_views.route("/restaurants", methods=["GET"], strict_slashes=False)
def get_restaurant():
    """Reterive all restaurants object"""
    restaurants = [obj.to_dict() for obj in storage.all("Restaurant").values()]
    return jsonify(restaurants), 200


@all_views.route("/restaurants/<restaurant_id>",
                 methods=['GET'], strict_slashes=False)
def get_restaurant_by_id(restaurant_id):
    """Reterive a restaurant object based on provided restaurant_id"""
    user = storage.get("Restaurant", restaurant_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict()), 200


@all_views.route("/restaurants/<restaurant_id>",
                 methods=["DELETE"], strict_slashes=False)
def delete_restaurant(restaurant_id):
    """Delete restaurant object based on provided restaurant_id"""
    user = storage.get('Restaurant', restaurant_id)
    if user is None:
        abort(404)
    user.delete()
    return jsonify({}), 200


@all_views.route("/restaurants", methods=["POST"], strict_slashes=False)
def create_restaurant():
    """Create a new restaurant object"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    elif "name" not in data:
        return jsonify({"error": "Missing name"}), 400
    elif "address" not in data:
        return jsonify({"error": "Missing address"}), 400
    elif 'description' not in data:
        return jsonify({"error": "Missing description"}), 400
    else:
        restaurant = Restaurant(**data)
        restaurant.save()
        return jsonify(restaurant.to_dict()), 201


@all_views.route("/restaurants/<restaurant_id>",
                 methods=["PUT"], strict_slashes=False)
def update_restaurant(restaurant_id):
    """Update a restaurant object based on provided user id"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    restaurant = storage.get('Restaurant', restaurant_id)
    if restaurant is None:
        abort(404)
    ignore = ('id', 'created_on', 'updated_on')
    for key in data.keys():
        if key not in ignore:
            setattr(restaurant, key, data[key])
    restaurant.save()
    return jsonify(restaurant.to_dict()), 200
