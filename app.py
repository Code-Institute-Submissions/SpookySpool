import os
import json
from flask import Flask
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

    genre_list = []
    genres = mongo.db.genres.find()
    for genre in genres:
        genre_list.append(genre["genre_name"])

    movies = mongo.db.movies.find()
    for movie in movies:
        for movie_genre in movie["genre"]:
            if movie_genre not in genre_list:
                mongo.db.genres.insert_one({"genre_name": movie_genre})
                genre_list.append(movie_genre)
    return "genres added"



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
