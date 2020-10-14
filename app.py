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
    all_movies = movies.find().count()
    scary_movies = movies.find({"$or": [{"genre": ObjectId("5f806ebc0727bbf597c35ba4")}, {"genre": ObjectId("5f806ebc0727bbf597c35ba5")}]})
    scary_movies_count = movies.find({"$or": [{"genre": ObjectId("5f806ebc0727bbf597c35ba4")}, {"genre": ObjectId("5f806ebc0727bbf597c35ba5")}]}).count()

    for movie in scary_movies:
        try:
            print(movie["keep"])
        except KeyError:
            movies.update_one({"_id": ObjectId(movie["_id"])}, {"$set": {"keep": "True"}})

    movie_count = movies.find({"keep": "True"}).count()

    return "correct movies to keep marked, marked movies = {}, scary movie total: {}".format(movie_count, scary_movies_count)
        


@app.route("/browse")
def browse_movies():

    movie_list = mongo.db.movies

    movies = movie_list.find().sort("year", -1).limit(60)

    return render_template("browse.html", movies=movies)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
