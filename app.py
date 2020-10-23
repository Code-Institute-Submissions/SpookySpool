import os
from flask import Flask, flash, render_template, redirect, request, url_for, session
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

    all_movies = mongo.db.movies.find()
    ratings = []

    for movie in all_movies:
        if movie["rating"] not in ratings:
            ratings.append(movie["rating"])
        else:
            continue

    return str(ratings)


# Login page and accociated functions

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


@app.route("/logout")
def logout():

    session["username"] = ""

    return redirect(url_for('login'))


# Browse & Movie pages

@app.route("/browse")
def browse_movies():

    movie_list = mongo.db.movies
    movies = movie_list.find().sort("year", -1).limit(10)

    if session["username"]:
        user = users.find_one({"username": session["username"]})
    else:
        flash("Sign in to create watchlists & more!")
        user=""

    return render_template("browse.html", movies=movies, user=user)


@app.route("/movie/<movie_id>")
def movie_page(movie_id):
    movie_data = movies.find_one({"_id": ObjectId(movie_id)})
    genre_data = genres.find()
    return render_template('movie_template.html', movie=movie_data, genres=genre_data)


# Add to watchlist/favourites and Remove from watchlist/favourites

@app.route("/watchlist/<movie_id>/redirect_from<page>")
def add_watchlist(movie_id, page):

    user = users.find_one({"username": session["username"]})
    user["watchlist"].append(ObjectId(movie_id))
    users.update_one({"username": session["username"]},
                     {"$set": {"watchlist": user["watchlist"]}})

    return redirect(url_for(f"{page}"))

@app.route("/remove_watchlist/<movie_id>/redirect_from<page>")
def remove_watchlist(movie_id, page):

    user = users.find_one({"username": session["username"]})
    user["watchlist"].remove(ObjectId(movie_id))
    users.update_one({"username": session["username"]},
                     {"$set": {"watchlist": user["watchlist"]}})

    return redirect(url_for(f"{page}"))


@app.route("/favourites/<movie_id>/redirect_from<page>")
def add_favourites(movie_id, page):

    user = users.find_one({"username": session["username"]})
    user["favourites"].append(ObjectId(movie_id))
    users.update_one({"username": session["username"]},
                     {"$set": {"favourites": user["favourites"]}})

    return redirect(url_for(f"{page}"))


@app.route("/remove_favourite/<movie_id>/redirect_from<page>")
def remove_favourite(movie_id, page):

    user = users.find_one({"username": session["username"]})
    user["favourites"].remove(ObjectId(movie_id))
    users.update_one({"username": session["username"]},
                     {"$set": {"favourites": user["favourites"]}})

    return redirect(url_for(f"{page}"))

@app.route("/user_submit")
def submit_movie():
    return render_template("movie_form.html", genres=genres.find())


# Inserts movies from the submit form into the database

@app.route("/insert_movie", methods=["POST"])
def insert_movie():

    user = users.find_one({"username": session["username"]})
    
    genre_list = []
    for genre in request.form.getlist("genre"):
        genre_list.append(ObjectId(genre))

    query = {"title:": request.form.get("title"),
             "rating": request.form.get("rating"),
             "year": request.form.get("year"),
             "metascore": request.form.get("metascore"),
             "img_url": request.form.get("img_url"),
             "languages": request.form.getlist("languages[]"),
             "actors": request.form.getlist("actors[]"),
             "genre": genre_list,
             "tagline": request.form.get("tagline"),
             "description": request.form.get("description"),
             "directors": request.form.getlist("directors[]"),
             "runtime": str(request.form.get("runtime")) + " min",
             "imdb_url": request.form.get("imdb_url"),
             "user_submitted": True,
             "user_id": ObjectId(user["_id"])
            }

    mongo.db.test_inserts.insert_one(query)

    #Adds the inserted movie id into the user's submitted movie array
    new_movie = users.find().sort("_id", -1)
    user["submitted_movies"].append(ObjectId(new_movie[0]["_id"]))
    users.update_one({"username": user["username"]},
                     {"$set": {"submitted_movies": user["submitted_movies"]}})

    return redirect(url_for("browse_movies"))

@app.route("/update/<movie_id>")
def update_movie(movie_id):

    return render_template("movie_update.html", genres=genres.find(),
                           movie=movies.find_one({"_id": movie_id}))


@app.route("/user/<username>")
def user_home(username):
    user_data = users.find_one({"username": username})
    favourite_movies = movies.find({"_id": {"$in": user_data["favourites"]}})

    return render_template("user_home.html", user=users.find_one({"username": username}), favourites=favourite_movies)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
