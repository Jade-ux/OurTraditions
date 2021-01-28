import os
from flask import (
    Flask, flash, render_template, redirect, 
    request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_traditions")
def get_traditions():
    traditions = list(mongo.db.traditions.find())
    return render_template("traditions.html", traditions=traditions)


@app.route("/search", methods=["GET", "POST"])
def search():
    keywords = request.form.get("keywords")
    countries = request.form.get("countries")
    traditions = list(mongo.db.traditions.find({"$text":{"$search": keywords}}))
    return render_template("traditions.html", traditions=traditions)


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # check if username exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
        }
        mongo.db.users.insert_one(register)

        # put the new user into 'session' cookie
        session["user"] = request.form.get("username").lower()
        flash("Registration Successful!")
        # once logged, redirect user to their profile page, using session cookie
        return redirect(url_for("profile", username=session["user"]))
    
    return render_template("register.html")

#login function
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # check if username exists and if it does, store it in a variable
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # ensure hashed password matches the user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for(
                        "profile", username=session["user"]))
            else:
                # invalid password match - we do not want to let them know 
                # exactly which they have wrong as that would make it easier to # brute force entries
                flash("The username/password you entered is incorrect, please try again")
                return redirect(url_for("login"))

        else:
             # if username doesn't exist
            flash("The username/password you entered is incorrect, please try again")
            return redirect(url_for("login")) 

    # acts as the else condition if the method is not POST
    return render_template("login.html")


@app.route("/user_profile/<username>", methods=["GET", "POST"])
def profile(username):
    traditions = list(mongo.db.traditions.find())
    # get the session user's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    if session["user"]:
        return render_template(
            "user_profile.html", username=username, traditions=traditions)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # removes the session cookie so that the user is logged out
    flash("You are now logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_tradition", methods=["GET", "POST"])
def add_tradition():
    if request.method == "POST":
        # collects the form fields and creates a dictionary
        tradition = {
            "tradition_name": request.form.get("tradition_name"),
            "category_name": request.form.get("category_name"),
            "group_name": request.form.get("group_name"),
            "country": request.form.get("country"),
            "tradition_description": request.form.get("tradition_description"),
            "created_by": session["user"]
            # "image": upload_image()
        }
        mongo.db.traditions.insert_one(tradition)
        flash("Your tradition has been added!")
        return redirect(url_for("get_traditions"))

    # if method is not POST then revert to the default method which is GET    
    categories = mongo.db.categories.find().sort("category_name", 1)
    groups = mongo.db.groups.find().sort("group_name", 1)
    return render_template("add_tradition.html", categories=categories)

# this code was inspired by this tutorial: 
# https://www.youtube.com/watch?v=6WruncSoCdI 
app.config["IMAGE_UPLOADS"] = "/workspace/OurTraditions/static/images/uploads"
app.config["VALID_IMAGE_EXTENSIONS"] = ["PNG", "JPG", "JPEG", "GIF"]

def valid_images(filename):
    if not "." in filename:
        return False

    extension = filename.rsplit(".", 1)[1]

    if extension.upper() in app.config["VALID_IMAGE_EXTENSIONS"]:
        return True
    else: 
        return False


@app.route("/upload_image", methods=["GET", "POST"])
def upload_image():
    if request.method == "POST":
        if request.files:
            image = request.files["image"]
            if image.filename == "":
                flash("Please choose an image with a filename")
                return redirect(request.url)

            if not valid_images(image.filename):
                flash("Please choose an image with a file type of either jpg, jpeg, png or gif")
                return redirect(request.url)

            else: 
                filename = secure_filename(image.filename)
                image.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))
            image.save(os.path.join(
                app.config["IMAGE_UPLOADS"], image.filename))
            flash("Your image has been uploaded")
            return redirect(request.url)
    return render_template("image_upload.html")


@app.route("/edit_tradition/<tradition_id>", methods=["GET", "POST"])
def edit_tradition(tradition_id):
    if request.method == "POST":
        # collects the form fields and creates a dictionary
        edit_tradition = {
            "tradition_name": request.form.get("tradition_name"),
            "category_name": request.form.get("category_name"),
            "group_name": request.form.get("group_name"),
            "country": request.form.get("country"),
            "tradition_description": request.form.get("tradition_description"),
            "created_by": session["user"]
        }
        mongo.db.traditions.update(
            {"_id": ObjectId(tradition_id)}, edit_tradition)
        flash("Your tradition has been updated.")

    # if method is not POST then revert to this default
    tradition = mongo.db.traditions.find_one({"_id": ObjectId(tradition_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    groups = mongo.db.groups.find().sort("group_name", 1)
    return render_template(
        "edit_tradition.html", tradition=tradition, categories=categories, groups=groups)


@app.route("/delete_tradition/<tradition_id>")
def delete_tradition(tradition_id):
    mongo.db.traditions.remove({"_id": ObjectId(tradition_id)})
    flash("Your tradition has been deleted.")
    return redirect(url_for("get_traditions"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
