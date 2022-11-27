#!/usr/bin/python3
"""
    Blueprint that handle all page route to make website
"""
from flask import Blueprint, render_template, request, redirect, flash
from flask_login import login_required, current_user
from models import storage

main = Blueprint("main", __name__)

def averageRate(rate):
    """Retervie the total rate of food review"""
    total = 0
    for num in rate:
        total += num
    return round(total / len(rate) if len(rate) > 0 else 0, 1)

@main.route("/")
def landing():
    """Reterive langing page"""
    return render_template("landing.html")

@main.route('/restaurants')
@login_required
def restaurants():
    """Reterive restaurant page"""
    restaurants = storage.all('Restaurant').values()
    # restaurant_image = "https://media-cdn.tripadvisor.com/media/photo-s/09/55/74/73/washington-hotel.jpg"

    return render_template("restaurant.html", restaurants= restaurants, 
                         user_id=current_user.id,
                           user_name=current_user.first_name, user_is_admin= current_user.is_admin)

# @main.route('/foods')
# def foods():
#     """Reterive foods pages"""
#     restaurant_id = request.args.get('restaurant_id')
#     restaurant = storage.get("Restaurant", restaurant_id)
#     foods = restaurant.foods
#     r = [f.id for f in foods]
    
#     # food_image = "https://i.pinimg.com/originals/23/04/c4/2304c46180dd7647078e2c42f87a8747.jpg"
#     return render_template("food.html", foods=foods, user_id=current_user.id,
#                            restaurant_name=restaurant.name, restaurant_id=restaurant.id,
#                            user_name=current_user.first_name, food_rate=4.6)



@main.route("/foods")
def foods():
    """Reterive foods pages"""
    restaurant_id = request.args.get("restaurant_id")
    restaurant = storage.get("Restaurant", restaurant_id)
    foods = restaurant.foods

    # I changed starting from this
    food_id_list = [food.id for food in foods]
    food_rate_list = []
    for food_id in food_id_list:
        food_item = storage.get("Food", food_id)
        reviews = food_item.reviews
        foodRate = [val.rate for val in reviews]
        food_rate_list.append(averageRate(foodRate))
    # ending to this
    
    # food_image = "https://i.pinimg.com/originals/23/04/c4/2304c46180dd7647078e2c42f87a8747.jpg"
    return render_template("food.html", food_rate_list=food_rate_list, foods=foods, user_id=current_user.id,
                           restaurant_name=restaurant.name, restaurant_id=restaurant.id,
                           user_name=current_user.first_name)


@main.route('/reviews')
def reviews():
    """Reterive reviews page"""
    restaurant_id = request.args.get("restaurant_id")
    food_id = request.args.get('food_id')
    food = storage.get("Food", food_id)
    restaurant = storage.get("Restaurant", restaurant_id)
    reviews = food.reviews
    foodRate = [val.rate for val in reviews]
    food_rate = averageRate(foodRate)
    restaurant_contact="+251 93939483"
    # food_image = "https://i.pinimg.com/originals/23/04/c4/2304c46180dd7647078e2c42f87a8747.jpg"
   
    return render_template("review.html", restaurant=restaurant, food_rate=food_rate, food=food,
                           user_id=current_user.id, user_name=current_user.first_name,
                           reviews=reviews)
