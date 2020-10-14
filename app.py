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
    movie_db = mongo.db.movies
    movies = movie_db.find()
    zombie_movies = []
    
    for movie in movies:
        if ("zombie" in str(movie["description"])) or ("Zombie" in str(movie["description"])):
            zombie_movies.append(movie["title"])
            movie_db.update({"_id": ObjectId(movie["_id"])},{"$addToSet":{"genre": "Zombie"}})
    
    length = len(zombie_movies)

    return str(length) + str(zombie_movies)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
