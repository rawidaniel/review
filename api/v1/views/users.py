#!/usr/bin/python3
'''
    RESTful API for class User
'''
from api.v1.views import all_views
from flask import jsonify, abort, request
from models import storage
from models.user import User


@all_views.route("/users", methods=['GET'], strict_slashes=False)
def get_users():
    """Reterive all users object"""
    users = [user.to_dict() for user in storage.all('User').values()]
    return jsonify(users), 200


@all_views.route("/users/<user_id>", methods=['GET'], strict_slashes=False)
def get_user_by_id(user_id):
    """Reterive a user object based on provided user_id"""
    user = storage.get("User", user_id)
    if user is None:
        abort(404)
    return jsonify(user.to_dict()), 200


@all_views.route("/users/<user_id>", methods=["DELETE"], strict_slashes=False)
def delete_user(user_id):
    """Delete user object based on provided user_id"""
    user = storage.get('User', user_id)
    if user is None:
        abort(404)
    user.delete()
    return jsonify({}), 200


@all_views.route("/users", methods=["POST"], strict_slashes=False)
def create_user():
    """Create a new user object"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    elif "first_name" not in data:
        return jsonify({"error": "Missing first name"}), 400
    elif "last_name" not in data:
        return jsonify({"error": "Missing last name"}), 400
    elif 'password' not in data:
        return jsonify({"error": "Missing password"}), 400
    elif 'email' not in data:
        return jsonify({"error": "Missing email"}), 400
    user_check = storage.get_user_by_email(data.get("email"))
    if user_check:
        return jsonify({"error": "email exists"}), 400
    user = User(**data)
    user.save()
    return jsonify(user.to_dict()), 201


@all_views.route("/users/<user_id>", methods=["PUT"], strict_slashes=False)
def update_user(user_id):
    """Update a user object based on provided user id"""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Not a JSON"}), 400
    user = storage.get('User', user_id)
    if user is None:
        abort(404)
    ignore = ('id', 'email', 'created_on', 'updated_on')
    for key in data.keys():
        if key not in ignore:
            setattr(user, key, data[key])
    user.save()
    return jsonify(user.to_dict()), 200
