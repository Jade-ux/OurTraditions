import os
from flask import (
    Flask, flash, render_template, redirect, 
    request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
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


@app.route("/user-profile/<username>", methods=["GET", "POST"])
def profile(username):
    # get the session user's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]

    if session["user"]:
        return render_template("user-profile.html", username=username)

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
            "country": request.form.get("country"),
            # this will allow the function to get multiple elements with the same name attribute, where we are storing an array
            "keywords": request.form.getlist("keywords"),
            "tradition_description": request.form.get("tradition_description"),
            "created_by": session["user"]
        }
        mongo.db.traditions.insert_one(tradition)
        flash("Your tradition has been added!")
        return redirect(url_for("get_traditions"))

    # if method is not POST then revert to the default method which is GET    
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("add_tradition.html", categories=categories)


@app.route("/edit_tradition/<tradition_id>", methods=["GET", "POST"])
def edit_tradition(tradition_id):
    tradition = mongo.db.traditions.find_one({"_id": ObjectId(tradition_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    return render_template("edit_tradition.html", tradition=tradition, categories=categories)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
