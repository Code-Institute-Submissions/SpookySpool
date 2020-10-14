import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "spooky_spool"
app.config["MONGO_URI"] = os.getenv("MONGODB_URI")

mongo = PyMongo(app)


@app.route("/")
def index():

    movies = mongo.db.movies
    keep_count = movies.find({"keep": "True"}).count()
    remove_count = movies.find({ "keep": {"$exists": False}}).count()
    all_count = movies.find().count()

    return "Movies to keep: {}, Movies to remove: {}, Movie total: {}".format(keep_count, remove_count, all_count)
        


@app.route("/browse")
def browse_movies():

    movie_list = mongo.db.movies

    movies = movie_list.find().sort("year", -1).limit(60)

    return render_template("browse.html", movies=movies)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
