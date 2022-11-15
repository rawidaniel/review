from flask import Blueprint, render_template, request, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user
from models import storage
from models.user import User

auth = Blueprint('auth', __name__)

@auth.route("/login")
def login():
    return render_template("login.html")

@auth.route("/login",methods=["POST"])
def login_post():
    email = request.form.get("email")
    password = request.form.get("password")
    remember = True if request.form.get("remember") else False

    user = storage.get_user_by_email(email=email)
    if not user or not check_password_hash(user.password, password):
        flash("Please provide correct credential details and try again.")
        return redirect(url_for("auth.login"))
    login_user(user, remember=remember)
    return redirect(url_for("main.profile"))

@auth.route("/signup")
def signup():
    return render_template("signup.html")

@auth.route("/signup", methods=["POST"])
def signup_post():
    email = request.form.get("email")
    firstname = request.form.get("firstname")
    lastname = request.form.get("lastname")
    password = request.form.get("password")
    confirmpassword = request.form.get("confirmpassword")

    user = storage.get_user_by_email(email=email)
    if user:
        flash("Email address already exist")
        return redirect(url_for("auth.signup"))

    if password != confirmpassword:
        flash("password don\'t match")
        return redirect(url_for("auth.signup"))
    user = User(email=email, first_name=firstname, last_name=lastname,
                password= generate_password_hash(password, method='sha256'))
    user.save()
    return redirect(url_for("auth.login"))

@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return render_template('index.html')