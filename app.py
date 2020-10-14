import os
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
    movie_db = mongo.db.movies
    genres = mongo.db.genres.find()

    for genre in genres:
        movie_db.update_many(
            {"genre": genre["genre_name"]},
            {"$set": {"genre.$": ObjectId(genre["_id"])}}
        )

    return "Genres updated in movie genre arrays to genre ids from genre collection"


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
