#!/usr/bin/python3
"""
    Blueprint that handle all page route to make website
"""
from flask import Blueprint, render_template, request, redirect, flash
from flask_login import login_required, current_user
from models import storage

main = Blueprint("main", __name__)


def rate_counter(rates):
    """Reterive dictionary of rate and their corresponding value"""
    count_dict = {}
    for i in range(5):
        count_dict[i + 1] = 0
    
    for rate in rates:
        rate = int(rate)

        if rate == 0:
            continue
        count_dict[rate] += 1
        
    return count_dict


def averageRate(rate):
    """Retervie the total rate of food review"""
    total = 0
    for num in rate:
        total += num
    return round(total / len(rate) if len(rate) > 0 else 0, 1)


@main.route("/")
def landing():
    """Reterive langing page"""
    return render_template("landing.html", user=current_user)


@main.route('/restaurants')
@login_required
def restaurants():
    """Reterive restaurant page"""
    restaurants = storage.all('Restaurant').values()
    return render_template("restaurant.html", restaurants=restaurants,
                           user_id=current_user.id,
                           user_name=current_user.first_name,
                           user_is_admin=current_user.is_admin)


@main.route("/foods")
def foods():
    """Reterive foods pages"""
    restaurant_id = request.args.get("restaurant_id")
    restaurant = storage.get("Restaurant", restaurant_id)
    foods = restaurant.foods

    food_id_list = [food.id for food in foods]
    food_rate_list = []
    for food_id in food_id_list:
        food_item = storage.get("Food", food_id)
        reviews = food_item.reviews
        foodRate = [val.rate for val in reviews]
        food_rate_list.append(averageRate(foodRate))
    return render_template("food.html", food_rate_list=food_rate_list,
                           foods=foods, user_id=current_user.id,
                           restaurant_name=restaurant.name,
                           restaurant_id=restaurant.id,
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
    rate_list = rate_counter(foodRate)
    rate_count = len(foodRate)
    if rate_count == 0:
        rate_count = 1
    return render_template("review.html", restaurant=restaurant,
                           food_rate=food_rate, food=food,
                           user_id=current_user.id, rate_list=rate_list, rate_count=rate_count, 
                           user_name=current_user.first_name,
                           reviews=reviews)
