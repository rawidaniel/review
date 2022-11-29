#!/usr/bin/python3
"""
    Blueprint that handle all login and signup authentication
"""
from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
from models import storage
from models.user import User

auth = Blueprint('auth', __name__)


@auth.route("/login")
def login():
    """Reterive login page"""
    if current_user.is_authenticated:
        return redirect(url_for("main.restaurants"))
    return render_template("login.html")


@auth.route("/login", methods=["POST"])
def login_post():
    """check the existing of user and route to restaurant or admin page"""
    email = request.form.get("email")
    password = request.form.get("password")
    remember = True if request.form.get("remember") else False

    user = storage.get_user_by_email(email=email)
    if not user or not check_password_hash(user.password, password):
        flash("Please provide correct credential details and try again.")
        return redirect(url_for("auth.login"))
    login_user(user, remember=remember)
    if current_user.is_admin:
        return redirect(url_for("admin.index"))
    return redirect(url_for("main.restaurants"))


@auth.route("/signup")
def signup():
    """Reterive signup page"""
    if current_user.is_authenticated:
        return redirect(url_for("main.restaurants"))
    return render_template("signup.html")


@auth.route("/signup", methods=["POST"])
def signup_post():
    """crate a new user for signup and route to login page"""
    email = request.form.get("email")
    firstname = request.form.get("first-name")
    lastname = request.form.get("last-name")
    password = request.form.get("password")
    confirmpassword = request.form.get("con-password")

    user = storage.get_user_by_email(email=email)
    if user:
        flash("Email address already exist")
        return redirect(url_for("auth.signup"))
    if password != confirmpassword:
        flash("password don\'t match")
        return redirect(url_for("auth.signup"))
    user = User(email=email, first_name=firstname, last_name=lastname,
                password=password)
    user.save()
    return redirect(url_for("auth.login"))


@auth.route("/logout")
@login_required
def logout():
    """Reterive landing page"""
    logout_user()
    return render_template('landing.html')
