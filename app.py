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
    movies = mongo.db.movies.find()
    for movie in movies:
        if not movie["genre"]:
            print(movie["title"])



    return "genres added"



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
