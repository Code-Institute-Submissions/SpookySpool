import os
import urllib.request
import ast
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


# Homepage
@app.route("/home")
@app.route("/")
def index():

    return render_template("home.html")


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
            flash("User doesn't exist")
        elif user_data["username"] and password != user_data["password"]:
            flash("Password incorrect")
        elif user_data["username"] and password == user_data["password"]:
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
            session["username"] = username
            return redirect(url_for("browse_movies", page_num=1))
        elif (username_check is not None):
            flash("Username is taken")
        elif (email_check is not None):
            flash("Email already exists")
        return redirect(url_for("login"))


@app.route("/logout")
def logout():

    session.pop('username', None)

    return redirect(url_for('login'))


# Browse & Movie pages
@app.route("/browse")
@app.route("/browse/page=<page_num>")
def browse_movies(page_num=1):

    movie_list = mongo.db.movies
    movies = movie_list.find().sort("year", -1)
    pages = int(movies.count()/40)+1

    index_start = (int(page_num)-1)*36
    index_end = int(page_num)*36

    if "username" in session.keys():
        user = users.find_one({"username": session["username"]})
    else:
        user = ""

    movie_genres = genres.find()

    return render_template("browse.html", movies=movies[index_start:index_end],
                           user=user, pages=pages, current_page=int(page_num),
                           genres=movie_genres)


# Search function
@app.route("/search-results/page=<page_num>/new-search=<query>",
           methods=["GET", "POST"])
def search(page_num, query):

    if request.method == "POST":

        # This searches the database for matches and filters out unused fields
        query = {}
        title = request.form.get("search-title")
        rating = request.form.getlist("rating")
        genre = request.form.getlist("genre")
        released_from = request.form.get("from")
        released_to = request.form.get("to")

        if title:
            query["title"] = {"$regex": title, "$options": "i"}
        if rating:
            query["rating"] = {"$in": rating}
        if genre:
            genre_list = []
            for genre in request.form.getlist("genre"):
                genre_list.append(ObjectId(genre))
            query["genre"] = {"$all": genre_list}
        if released_from and released_to:
            query["year"] = {"$gte": released_from, "$lte": released_to}
        elif released_from and not released_to:
            query["year"] = {"$gte": released_from}
        elif not released_from and released_to:
            query["year"] = {"$lte": released_to}
        results = movies.find(query)
        sorted_results = results.sort("year", -1)

    else:
        # This converts the query string into a dictionary
        query = query.replace("ObjectId('", "'").replace(
            "')", "'").replace("\n", ",")
        query = ast.literal_eval(query)

        # This added the ObjectId() back onto genres if in the query
        if "genre" in query.keys():
            for x in query["genre"]["$all"]:
                position = query["genre"]["$all"].index(x)
                query["genre"]["$all"][position] = ObjectId(x)

        results = movies.find(query)
        sorted_results = results.sort("year", -1)

    flash(f"{results.count()}", "matches")
    pages = int(results.count()/40)+1
    index_start = (int(page_num)-1)*36
    index_end = int(page_num)*36

    if "username" in session.keys():
        user = users.find_one({"username": session["username"]})
    else:
        user = ""

    movie_genres = genres.find()
    return render_template("results.html", current_page=int(page_num),
                           movies=sorted_results[index_start:index_end],
                           genres=movie_genres, user=user, pages=pages,
                           query=query)


@app.route("/movie/<movie_id>")
def movie_page(movie_id):
    movie_data = movies.find_one({"_id": ObjectId(movie_id)})
    genre_data = genres.find()
    if "username" in session.keys():
        user = users.find_one({"username": session["username"]})
    else:
        user = ""
    return render_template('movie_template.html', movie=movie_data,
                           genres=genre_data, user=user)


# Add to watchlist/favourites and Remove from watchlist/favourites
@app.route("/watchlist/<movie_id>/redirect=<page>/<value>")
def add_watchlist(movie_id, page, value):
    user = users.find_one({"username": session["username"]})
    user["watchlist"].append(ObjectId(movie_id))
    users.update_one({"username": session["username"]},
                     {"$set": {"watchlist": user["watchlist"]}})
    flash(u'Movie Added to Watchlist', 'list_function')
    if page == "browse_movies":
        return redirect(url_for(f"{page}", page_num=value))
    elif page == "user_home":
        return redirect(url_for(f"{page}", username=value))
    elif page == "search":
        return redirect(url_for(f"{page}", page_num=1, query=value))
    else:
        return redirect(url_for(f"{page}", movie_id=movie_id))


@app.route("/remove_watchlist/<movie_id>/redirect=<page>/<value>")
def remove_watchlist(movie_id, page, value):

    user = users.find_one({"username": session["username"]})
    user["watchlist"].remove(ObjectId(movie_id))
    users.update_one({"username": session["username"]},
                     {"$set": {"watchlist": user["watchlist"]}})
    flash(u'Movie Removed from Watchlist', 'list_function')

    if page == "browse_movies":
        return redirect(url_for(f"{page}", page_num=value))
    elif page == "user_home":
        return redirect(url_for(f"{page}", username=value))
    elif page == "search":
        return redirect(url_for(f"{page}", page_num=1, query=value))
    else:
        return redirect(url_for(f"{page}", movie_id=movie_id))


@app.route("/favourites/<movie_id>/redirect=<page>/<value>")
def add_favourites(movie_id, page, value):

    user = users.find_one({"username": session["username"]})
    user["favourites"].append(ObjectId(movie_id))
    users.update_one({"username": session["username"]},
                     {"$set": {"favourites": user["favourites"]}})
    flash('Movie Added to Favourites', 'list_function')

    if page == "browse_movies":
        return redirect(url_for(f"{page}", page_num=value))
    elif page == "user_home":
        return redirect(url_for(f"{page}", username=value))
    elif page == "search":
        return redirect(url_for(f"{page}", page_num=1, query=value))
    else:
        return redirect(url_for(f"{page}", movie_id=movie_id))


@app.route("/remove_favourite/<movie_id>/redirect=<page>/<value>")
def remove_favourite(movie_id, page, value):

    user = users.find_one({"username": session["username"]})
    user["favourites"].remove(ObjectId(movie_id))
    users.update_one({"username": session["username"]},
                     {"$set": {"favourites": user["favourites"]}})
    flash(u'Movie Removed from Favourites', 'list_function')

    if page == "browse_movies":
        return redirect(url_for(f"{page}", page_num=value))
    elif page == "user_home":
        return redirect(url_for(f"{page}", username=value))
    elif page == "search":
        return redirect(url_for(f"{page}", page_num=1, query=value))
    else:
        return redirect(url_for(f"{page}", movie_id=movie_id))


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

    img_url = request.form.get("img_url")
    try:
        urllib.request.urlopen(img_url).getcode()
    except urllib.error.HTTPError:
        img_url = ""
    except ValueError:
        img_url = ""

    query = {"title": request.form.get("title"),
             "rating": request.form.get("rating"),
             "year": request.form.get("year"),
             "metascore": request.form.get("metascore"),
             "img_url": img_url,
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
    genre_list = []
    for genre in request.form.getlist("genre"):
        genre_list.append(ObjectId(genre))

    img_url = request.form.get("img_url")
    try:
        urllib.request.urlopen(img_url).getcode()
    except urllib.error.HTTPError:
        img_url = ""
    except ValueError:
        img_url = ""

    updated_movie = {"title": request.form.get("title"),
                     "rating": request.form.get("rating"),
                     "year": request.form.get("year"),
                     "metascore": request.form.get("metascore"),
                     "img_url": img_url,
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


# Remove movie
@app.route("/delete/<movie_id>")
def delete_movie(movie_id):
    username = session["username"]
    user = users.find_one({"username": username})

    movies.delete_one({"_id": ObjectId(movie_id)})

    user["submitted_movies"].remove(ObjectId(movie_id))
    users.update_one({"username": username},
                     {"$set": {"submitted_movies": user["submitted_movies"]}})

    return redirect(url_for("user_home", username=username))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
