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

#Homepage
@app.route("/home")
@app.route("/")
def index():

    return (render_template("home.html"))


# Login page and sign-in/logout functions
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
            return redirect(url_for("browse_movies", page_num=1))
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
                "submitted_movies": []
            })
            print("user added")
            return redirect(url_for("browse_movies", page_num=1))
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
@app.route("/browse/page=<page_num>")
def browse_movies(page_num):

    movie_list = mongo.db.movies
    movies = movie_list.find().sort("year", -1)
    pages = int(movies.count()/40)+1

    index_start = (int(page_num)-1)*36
    index_end = int(page_num)*36

    if session["username"]:
        user = users.find_one({"username": session["username"]})
    else:
        flash("Sign in to create watchlists & more!")
        user = ""

    return render_template("browse.html", movies=movies[index_start:index_end], user=user, pages=pages, current_page=int(page_num))


@app.route("/search", methods=["GET"])

@app.route("/movie/<movie_id>")
def movie_page(movie_id):
    movie_data = movies.find_one({"_id": ObjectId(movie_id)})
    genre_data = genres.find()
    return render_template('movie_template.html', movie=movie_data, genres=genre_data)


# Add to watchlist/favourites and Remove from watchlist/favourites
@app.route("/watchlist/<movie_id>/redirect=<page>/<value>")
def add_watchlist(movie_id, page, value):
    user = users.find_one({"username": session["username"]})
    user["watchlist"].append(ObjectId(movie_id))
    users.update_one({"username": session["username"]},
                     {"$set": {"watchlist": user["watchlist"]}})
    if page == "browse_movies":
        return redirect(url_for(f"{page}", page_num=value))
    elif page == "user_home":
        return redirect(url_for(f"{page}", username=value))


@app.route("/remove_watchlist/<movie_id>/redirect=<page>/<value>")
def remove_watchlist(movie_id, page, value):

    user = users.find_one({"username": session["username"]})
    user["watchlist"].remove(ObjectId(movie_id))
    users.update_one({"username": session["username"]},
                     {"$set": {"watchlist": user["watchlist"]}})

    if page == "browse_movies":
        return redirect(url_for(f"{page}", page_num=value))
    elif page == "user_home":
        return redirect(url_for(f"{page}", username=value))


@app.route("/favourites/<movie_id>/redirect=<page>/<value>")
def add_favourites(movie_id, page, value):

    user = users.find_one({"username": session["username"]})
    user["favourites"].append(ObjectId(movie_id))
    users.update_one({"username": session["username"]},
                     {"$set": {"favourites": user["favourites"]}})

    if page == "browse_movies":
        return redirect(url_for(f"{page}", page_num=value))
    elif page == "user_home":
        return redirect(url_for(f"{page}", username=value))


@app.route("/remove_favourite/<movie_id>/redirect=<page>/<value>")
def remove_favourite(movie_id, page, value):

    user = users.find_one({"username": session["username"]})
    user["favourites"].remove(ObjectId(movie_id))
    users.update_one({"username": session["username"]},
                     {"$set": {"favourites": user["favourites"]}})

    if page == "browse_movies":
        return redirect(url_for(f"{page}", page_num=value))
    elif page == "user_home":
        return redirect(url_for(f"{page}", username=value))


@app.route("/user_submit")
def submit_movie():
    return render_template("movie_form.html", genres=genres.find())


# User home page
@app.route("/user/<username>")
def user_home(username):
    user = users.find_one({"username": username})
    watchlist = movies.find({"_id": {"$in": user["watchlist"]}})
    favourites = movies.find({"_id": {"$in": user["favourites"]}})
    submitted = movies.find({"_id": {"$in": user["submitted_movies"]}})

    return render_template("user_home.html", user=user, favourites=favourites,
                           watchlist=watchlist, submitted=submitted)


# Inserts movies from the submit form into the database
@app.route("/insert_movie", methods=["POST"])
def insert_movie():

    user = users.find_one({"username": session["username"]})

    genre_list = []
    for genre in request.form.getlist("genre"):
        genre_list.append(ObjectId(genre))

    query = {"title": request.form.get("title").lower(),
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

    mongo.db.movies.insert_one(query)

    # Adds the inserted movie id into the user's submitted movie array

    inserted_movie = movies.find(
        {"user_id": ObjectId(user["_id"])}).sort("_id", -1)
    user["submitted_movies"].append(ObjectId(inserted_movie[0]["_id"]))
    users.update_one({"username": user["username"]},
                     {"$set": {"submitted_movies": user["submitted_movies"]}})

    return redirect(url_for("browse_movies", page_num=1))


# Update form for movies already in the database
@app.route("/update/<movie_id>")
def update_movie(movie_id):

    return render_template("movie_update.html", genres=genres.find(),
                           movie=movies.find_one({"_id": ObjectId(movie_id)}))


# Inserts updated movies from the update form into the database

@app.route("/insert_update/<movie_id>", methods=["POST"])
def insert_update(movie_id):
    print(movie_id)
    genre_list = []
    for genre in request.form.getlist("genre"):
        genre_list.append(ObjectId(genre))

    updated_movie = {"title": request.form.get("title").lower(),
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
                     "imdb_url": request.form.get("imdb_url")
                     }

    mongo.db.movies.update_one({"_id": ObjectId(movie_id)},
                               {"$set": updated_movie})

    return redirect(url_for("movie_page", movie_id=movie_id))





if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
