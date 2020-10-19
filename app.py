import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "spooky_spool"
app.config["MONGO_URI"] = os.getenv("MONGODB_URI")
app.secret_key = os.getenv("SECRET_KEY")

mongo = PyMongo(app)

movies = mongo.db.movies
users = mongo.db.users
genres = mongo.db.genres

@app.route("/")
def index():

    keep_count = movies.find({"keep": "True"}).count()
    remove_count = movies.find({"keep": {"$exists": False}}).count()
    all_count = movies.find().count()

    remove_movies = movies.find({"keep": {"$exists": False}})

    for movie in remove_movies:
        movies.delete_one({"_id": ObjectId(movie["_id"])})

    return "Movies to keep: {}, Movies to remove: {}, Movie total: {}".format(keep_count, remove_count, all_count)


@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/login/%", methods=["POST"])
def attempt_login():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        user_data = users.find_one({"username": username})

        if user_data is None:
            print("user doesn't exist")
        elif user_data["username"] and password != user_data["password"]:
            print("password incorrect")
        elif user_data["username"] and password == user_data["password"]:
            print("login succesful")
            session["username"] = username
            return redirect(url_for("browse_movies"))
        return redirect(url_for("login"))


@app.route("/login/sign_up", methods=["POST"])
def sign_up():
    if request.method == "POST":
        username = request.form.get('username')
        email = request.form.get('email')
        username_check = mongo.db.users.find_one({"username": username})
        email_check = mongo.db.users.find_one({"email": email})

        if (username_check is None and email_check is None):
            users.insert_one({
                "email": request.form.get('email'),
                "username": request.form.get('username'),
                "password": request.form.get('password'),
                "watchlist": [],
                "favourites": [],
                "user_submitted_movies": []
            })
            print("user added")
            return redirect(url_for("browse_movies"))
        elif (username_check is not None):
            print("username is taken")
        elif (email_check is not None):
            print("email is taken")
        return redirect(url_for("login"))


@app.route("/browse")
def browse_movies():

    movie_list = mongo.db.movies

    movies = movie_list.find().sort("year", -1).limit(10)

    return render_template("browse.html", movies=movies)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
