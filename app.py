import os
import boto3, botocore
from botocore.client import Config
from flask import (
    Flask, flash, render_template, redirect,
    request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import secure_filename
from io import BytesIO
from PIL import Image, ImageOps
if os.path.exists("env.py"):
    import env

# image extensions allowed
VALID_IMAGE_EXTENSIONS = ["PNG", "JPG", "JPEG", "GIF"]


# Amazon S3 access
S3_BUCKET = os.environ.get("S3_BUCKET")
S3_KEY = os.environ.get("S3_ACCESS_KEY")
S3_SECRET = os.environ.get("S3_SECRET_ACCESS_KEY")
S3_LOCATION = os.environ.get("S3_LOCATION")

s3 = boto3.client(
    "s3",
    aws_access_key_id=S3_KEY,
    aws_secret_access_key=S3_SECRET
)

app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


# Image upload
""" Help from:
Tutorial here:
https://www.zabana.me/notes/flask-tutorial-upload-files-amazon-s3
Code with thanks to (slightly modified):
https://github.com/Edb83/self-isolution/blob/master/app.py

"""


def valid_images(filename):
    if "." not in filename:
        return False

    extension = filename.rsplit(".", 1)[1]

    if extension.upper() in VALID_IMAGE_EXTENSIONS:
        return True
    else:
        return False


def upload_file():
    """
    Checks if the file is not empty, and is an allowed file type,
    if it is, sanitize the file name with Werkzeug's secure
    filename and then call upload_file_to_s3(). Return the
    output and convert to a string that can be saved in Mongo DB.

    """
    output = ""

    file = request.files["trad_image"]

    if file.filename == "":
        flash("Please select a file")
        output = ""

    if not valid_images(file.filename):
        flash(
            "Your image was not the correct file type please choose another.")
        output = ""

    else:
        file.filename = secure_filename(file.filename)
        output = upload_file_to_s3(file)
        return str(output)


def resize_image(file):

    """ Code with thanks to:
    https://github.com/Edb83/self-isolution/blob/master/app.py

    """
    # Load the image received through the submitted form
    raw_image = Image.open(file)

    # Save its format (as not copied on creation of new image)
    saved_format = raw_image.format

    # Read EXIF data to handle portrait images being rotated
    new_image = ImageOps.exif_transpose(raw_image)

    # Reapply raw_image format so that it can be resized
    new_image.format = saved_format

    # Resize image and set max size on either axis to 500px
    new_image.thumbnail((500, 500))

    # Save the image to an in-memory file
    in_mem_file = BytesIO()
    new_image.save(in_mem_file, format=new_image.format)

    # 'Rewind' the file-like object to prevent 0kb-sized files
    in_mem_file.seek(0)

    return in_mem_file


def upload_file_to_s3(file):
    """ Help from:
    Tutorial here:
    https://www.zabana.me/notes/flask-tutorial-upload-files-amazon-s3
    And:
    https://github.com/Edb83/self-isolution/blob/master/app.py

    """
    try:
        image_for_upload = resize_image(file)

        # Upload image to s3
        s3.upload_fileobj(
            image_for_upload,
            S3_BUCKET,
            file.filename,
            ExtraArgs={
                'ACL': 'public-read'
            }
        )

    except Exception as e:
        print("Oops, that didn't work: ", e)
        return e

    return "{}{}".format(S3_LOCATION, file.filename)


"""
Takes the searchCriteria from the search route
decorator and searches the database on that criteria

"""


def render_search_results(searchCriteria):
    traditions = list(
            mongo.db.traditions.find({"$text": {"$search": searchCriteria}}))
    categories_list = mongo.db.traditions.distinct("category_name")
    countries_list = mongo.db.traditions.distinct("country_name")
    groups_list = mongo.db.traditions.distinct(
            "group_name")
    return render_template(
        "search_results.html",
        traditions=traditions,
        categories_list=categories_list,
        countries_list=countries_list,
        groups_list=groups_list)


# Route decorators


@app.route("/")
@app.route("/get_traditions")
def get_traditions():
    traditions = list(mongo.db.traditions.find().sort("_id", -1))
    categories_list = mongo.db.traditions.distinct("category_name")
    countries_list = mongo.db.traditions.distinct("country_name")
    groups_list = mongo.db.traditions.distinct("group_name")
    return render_template(
        "traditions.html",
        traditions=traditions,
        categories_list=categories_list,
        countries_list=countries_list,
        groups_list=groups_list)


@app.route("/search", methods=["GET", "POST"])
def search():
    keywords = request.form.get("keywords")
    if keywords == "":
        flash("Please enter a keyword")
        traditions = list(mongo.db.traditions.find())
        return render_template(
            "traditions.html",
            traditions=traditions)
    
    else:
        return render_search_results(keywords)


@app.route("/search_country", methods=["GET", "POST"])
def search_country():
    country = request.form.get("country")
    if country == "":
        flash("Please enter a country")
        traditions = list(mongo.db.traditions.find())
        return render_template(
            "traditions.html",
            traditions=traditions)

    else:
        return render_search_results(country)


@app.route("/search_category", methods=["GET", "POST"])
def search_category():
    category = request.form.get("category")
    if category == "":
        flash("Please enter a category")
        traditions = list(mongo.db.traditions.find())
        return render_template("traditions.html",
            traditions=traditions)

    else:
        return render_search_results(category)


@app.route("/search_group", methods=["GET", "POST"])
def search_group():
    group = request.form.get("group")
    if group == "":
        flash("Please enter a group")
        traditions = list(mongo.db.traditions.find())
        return render_template(
            "traditions.html",
            traditions=traditions)
    
    else:
        return render_search_results(group)

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
        # once logged, redirect user to their profile page,
        # using session cookie
        return redirect(url_for("profile", username=session["user"]))

    return render_template("register.html")


# login function
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
                # exactly which they have wrong as that would make it easier to
                # brute force entries
                flash(
                    "The username/password you entered is incorrect, please try again")
                return redirect(url_for("login"))

        else:
            # if username doesn't exist
            flash(
                "The username/password you entered is incorrect, please try again")
            return redirect(url_for("login")) 

    # acts as the else condition if the method is not POST
    return render_template("login.html")


@app.route("/user_profile/<username>", methods=["GET", "POST"])
def profile(username):
    traditions = list(mongo.db.traditions.find())
    # checks if user is logged in before taking them to the profile
    if "user" not in session:
        flash("Please log in to view your profile")
        return redirect(url_for("login"))

    else:
        if session["user"]:
            # get the session user's username from the database
            username = mongo.db.users.find_one(
                {"username": session["user"]})["username"]
            return render_template(
                "user_profile.html", username=username, traditions=traditions)


@app.route("/logout")
def logout():
    # removes the session cookie so that the user is logged out
    flash("You are now logged out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_tradition", methods=["GET", "POST"])
def add_tradition():
    if "user" not in session:
        flash("Please log in to add a tradition")
        return redirect(url_for("login"))

    else:
        if request.method == "POST":
            # collects the form fields and creates a dictionary
            tradition = {
                "tradition_name": request.form.get("tradition_name"),
                "category_name": request.form.get("category_name"),
                "group_name": request.form.get("group_name"),
                "country_name": request.form.get(
                    "country_name"),
                "tradition_description": request.form.get(
                    "tradition_description"),
                "trad_image": upload_file(),
                "created_by": session["user"],
                # "vote_count": 0,
            }
            mongo.db.traditions.insert_one(tradition)
            flash("Your tradition has been added!")
            return redirect(url_for("get_traditions"))

    # if method is not POST, revert to the default method - GET
    categories = mongo.db.categories.find().sort("category_name", 1)
    groups = mongo.db.groups.find().sort("group_name", 1)
    countries = mongo.db.countries.find().sort("country_name", 1)
    return render_template(
        "add_tradition.html",
        categories=categories, groups=groups, countries=countries)


@app.route("/edit_tradition/<tradition_id>", methods=["GET", "POST"])
def edit_tradition(tradition_id):
    if request.method == "POST":
        tradition = mongo.db.traditions.find_one(
                    {"_id": ObjectId(tradition_id)})
        trad_owner = tradition["created_by"]
        # check if user is logged in, if not flash message and redirect to login 
        if "user" not in session: 
            flash("Please log in to edit your traditions")
            return redirect(url_for("login"))
        
        # check if user is the tradition owner
        if session["user"] != trad_owner:
            traditions = list(mongo.db.traditions.find())
            username = mongo.db.users.find_one(
            {"username": session["user"]})["username"]
            flash("You are trying to edit someone else's tradition!")
            return render_template(
                "user_profile.html", username=username, traditions=traditions)

        else: 
            new_image = request.form.get("trad_image")
            if new_image == "":
                edited_image = tradition["trad_image"]

            else:
                edited_image = upload_file()

        # collects the form fields and edits the tradition
        edit_tradition = {
            "tradition_name": request.form.get("tradition_name"),
            "category_name": request.form.get("category_name"),
            "group_name": request.form.get("group_name"),
            "country_name": request.form.get("country_name"),
            "tradition_description": request.form.get("tradition_description"),
            "created_by": session["user"],
            "trad_image": edited_image,
        }
        mongo.db.traditions.update(
            {"_id": ObjectId(tradition_id)}, edit_tradition)
        flash("Your tradition has been updated.")

    # if method is not POST then revert to this default
    tradition = mongo.db.traditions.find_one({"_id": ObjectId(tradition_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    groups = mongo.db.groups.find().sort("group_name", 1)
    countries = mongo.db.countries.find().sort("country_name", 1)
    return render_template(
        "edit_tradition.html",
        tradition=tradition,
        categories=categories,
        groups=groups,
        countries=countries)


@app.route("/delete_tradition/<tradition_id>")
def delete_tradition(tradition_id):
    tradition = mongo.db.traditions.find_one(
                {"_id": ObjectId(tradition_id)})
    trad_owner = tradition["created_by"]
    if "user" not in session: 
        flash("Please log in to delete your traditions")
        return redirect(url_for("login"))

    else: 
        mongo.db.traditions.remove({"_id": ObjectId(tradition_id)})
        flash("Your tradition has been deleted.")
        return redirect(url_for("get_traditions"))
        

if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)

