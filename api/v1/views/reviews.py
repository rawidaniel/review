# #!/usr/bin/python3
'''
    RESTful API for class Review
'''
from flask import jsonify, abort, request
from models import storage
from api.v1.views import all_views
from models.review import Review

# @all_views.route('/api/review', methods=["GET", "POST", "DELETE"])
# def review():
#         if request.method == "POST":
#             print(request.json["review_text"])
#             result = {'status': 'success'}
#             return result, 201
#         elif request.method == "DELETE":
#             print("review deleted")
#             result = {'status': 'success'}
#             return result, 204
#         elif request.method == "GET":
#             keys = ["rate", "review"]
#             values = [3, "I liked it so far"]
#             user_review = {}

#             for i in range(len(keys)):
#                 user_review[keys[i]] = values[i]

#             return jsonify(user_review)
# @all_views.route('/api/v1/review/rate', methods=["POST"])
# def rate():
#         print(request.json["rate"])
#         result = {'status': 'success'}
#         return result, 201


@all_views.route('/foods/<food_id>/reviews', methods=['GET'],
                 strict_slashes=False)
def get_review_by_food(food_id):
    '''
        return reviews by food, json form
    '''
    food = storage.get("Food", food_id)
    if food is None:
        abort(404)
    review_list = [r.to_dict() for r in food.reviews]
    return jsonify(review_list), 200


@all_views.route('/reviews/<review_id>', methods=['GET'], strict_slashes=False)
def get_review_id(review_id):
    '''
        return review given its id using GET
    '''
    review = storage.get("Review", review_id)
    if review is None:
        abort(404)
    return jsonify(review.to_dict()), 200


@all_views.route('/reviews/<review_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_review(review_id):
    '''
        delete review obj given review_id
    '''
    review = storage.get("Review", review_id)
    if review is None:
        abort(404)
    review.delete()
    return jsonify({}), 200


@all_views.route('/foods/<food_id>/reviews', methods=['POST'],
                 strict_slashes=False)
def create_review(food_id):
    '''
        create new review obj through food association using POST
    '''
    if storage.get("Food", food_id) is None:
        abort(404)
    elif not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    elif "user_id" not in request.get_json():
        return jsonify({"error": "Missing user_id"}), 400
    elif storage.get("User", request.get_json()["user_id"]) is None:
        abort(404)
    elif "text" not in request.get_json():
        return jsonify({"error": "Missing text"}), 400
    else:
        data = request.get_json()
        obj = Review(**data)
        obj.food_id = food_id
        obj.save()
        return jsonify(obj.to_dict()), 201


@all_views.route('/reviews/<review_id>', methods=['PUT'], strict_slashes=False)
def update_review(review_id):
    '''
        update review object using PUT
    '''
    obj = storage.get("Review", review_id)
    if obj is None:
        abort(404)
    elif not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    else:
        obj_data = request.get_json()
        ignore = ("id", "user_id", "food_id", "created_at", "updated_at")
        for k in obj_data.keys():
            if k in ignore:
                pass
            else:
                setattr(obj, k, obj_data[k])
        obj.save()
        return jsonify(obj.to_dict()), 200