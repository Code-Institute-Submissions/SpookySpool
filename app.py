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

with open("data/movie.json", "r") as jason_data:
    data = json.load(jason_data)


@app.route("/")
def index():
    movies = mongo.db.movies

    movies.insert_many(data)



    return "genres added"



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
