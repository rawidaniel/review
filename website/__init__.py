#!/usr/bin/python3
"""
Initalize flask application for website
"""
from flask import Flask, request, jsonify, redirect, url_for,\
        flash, render_template
from flask_login import LoginManager, current_user
from flask_admin import Admin, AdminIndexView
from flask_admin.contrib.sqla import ModelView
import os
from werkzeug.utils import secure_filename


def create_app():
    """Create Flask instance"""
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "secret_key_goes_here"
    UPLOAD_FOLDER = 'website/static/images/uploads/'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

    ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    @app.teardown_appcontext
    def close_db(error):
        """ Remove the current SQLAlchemy Session """
        storage.close()

    def allowed_file(filename):
        """Reterive true for allowed extensions or false"""
        return '.' in filename and filename.rsplit('.', 1)[1].lower()\
               in ALLOWED_EXTENSIONS

    @app.route("/uploadphoto", methods=["POST", "GET"])
    def uploadphoto():
        """Upload image into specified directory on filesystem"""
        if request.method == 'POST':
            if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
            file = request.files['file']
            if file.filename == '':
                flash('No image selected for uploading')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                flash('Image successfully uploaded and displayed below')
                return render_template('uploadphoto.html', filename=filename)
            else:
                flash('Allowed image types are - png, jpg, jpeg, gif')
                return redirect(request.url)
        return render_template("uploadphoto.html")

    from models import storage
    from models.food import Food
    from models.restaurant import Restaurant
    from models.review import Review
    from models.user import User

    class MyAdminIndexView(AdminIndexView):
        """administrative interface index page"""
        def is_accessible(self):
            """method to add permission checks"""
            if current_user.is_admin is True:
                return current_user.is_authenticated

        def inaccessible_callback(self, name, **kwargs):
            """Handle the response to inaccessible views"""
            if current_user.is_admin is False:
                return redirect(url_for("main.restaurants"))

    admin = Admin(app, 'Addisreview', url='/restaurants',
                  index_view=MyAdminIndexView(name="Home"))
    admin.add_view(ModelView(User, storage.session()))
    admin.add_view(ModelView(Food, storage.session()))
    admin.add_view(ModelView(Review, storage.session()))
    admin.add_view(ModelView(Restaurant, storage.session()))
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        """Reterive user object from the user ID stored in the session"""
        return storage.get_user_by_id(user_id)

    @app.route('/api/rate', methods=["POST"])
    def rate():
        print(request.json["rate"])
        result = {'status': 'success'}
        return result, 201

    @app.route('/api/review', methods=["GET", "POST", "DELETE"])
    def review():
        if request.method == "POST":
            print(request.json["review_text"])
            result = {'status': 'success'}
            return result, 201
        elif request.method == "DELETE":
            print("review deleted")
            result = {'status': 'success'}
            return result, 204
        elif request.method == "GET":
            keys = ["rate", "review"]
            values = [3, "I liked it so far"]
            user_review = {}

            for i in range(len(keys)):
                user_review[keys[i]] = values[i]

            return jsonify(user_review)
    return app
