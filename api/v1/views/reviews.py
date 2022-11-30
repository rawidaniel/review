# #!/usr/bin/python3
'''
    RESTful API for class Review
'''
from flask import jsonify, abort, request
from models import storage
from api.v1.views import all_views
from models.review import Review


@all_views.route("/reviews", methods=['GET'], strict_slashes=False)
def get_all_reviews():
    """Reterive all reviews object"""
    reviews = [review.to_dict() for review in storage.all('Review').values()]
    return jsonify(reviews), 200


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
    user_id = request.get_json()
    user_id = user_id["user_id"]
    review_user_id = [review.user_id for review in storage.all('Review').values()\
                      if review.food_id == food_id]
    if user_id in review_user_id:
        print('user find')
        abort(404)
    elif storage.get("Food", food_id) is None:
        abort(404)
    elif not request.get_json():
        return jsonify({"error": "Not a JSON"}), 400
    elif "user_id" not in request.get_json():
        return jsonify({"error": "Missing user_id"}), 400
    elif storage.get("User", request.get_json()["user_id"]) is None:
        abort(404)
    elif "rate" not in request.get_json():
        return jsonify({"error": "Missing rate"}), 400
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
