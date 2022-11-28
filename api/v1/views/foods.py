#!/usr/bin/python3
'''
    RESTful API for class Food
'''
from models import storage
from api.v1.views import all_views
from flask import jsonify, abort, request
from models.food import Food


@all_views.route("/foods", methods=["GET"], strict_slashes=False)
def get_food():
    """Reterive all foods object"""
    foods = [obj.to_dict() for obj in storage.all("Food").values()]
    return jsonify(foods), 200


@all_views.route("/foods/<food_id>", methods=['GET'], strict_slashes=False)
def get_food_by_id(food_id):
    """Reterive a food object based on provided food_id"""
    food = storage.get("Food", food_id)
    if food is None:
        abort(404)
    return jsonify(food.to_dict()), 200


@all_views.route("/foods/<food_id>", methods=["DELETE"], strict_slashes=False)
def delete_food(food_id):
    """Delete food object based on provided food_id"""
    food = storage.get('Food', food_id)
    if food is None:
        abort(404)
    food.delete()
    return jsonify({}), 200


@all_views.route("foods", methods=["POST"], strict_slashes=False)
def create_food():
    """Create a new food object"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    elif "name" not in data:
        return jsonify({"error": "Missing name"}), 400
    elif "price" not in data:
        return jsonify({"error": "Missing price"}), 400
    elif 'recipe' not in data:
        return jsonify({"error": "Missing recipe"}), 400
    elif 'description' not in data:
        return jsonify({"error": "Missing description"}), 400
    else:
        food = Food(**data)
        food.save()
        return jsonify(food.to_dict()), 201


@all_views.route("/foods/<food_id>", methods=["PUT"], strict_slashes=False)
def update_food(food_id):
    """Update a food object based on provided user id"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    food = storage.get('Food', food_id)
    if food is None:
        abort(404)
    ignore = ('id', 'created_on', 'updated_on')
    for key in data.keys():
        if key not in ignore:
            setattr(food, key, data[key])
    food.save()
    return jsonify(food.to_dict()), 200
