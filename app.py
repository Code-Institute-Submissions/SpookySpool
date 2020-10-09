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
    not_horror = mongo.db.movies.find({"genre": {"$ne": "Horror"}})
    for movie in not_horror:
        mongo.db.movies.remove({"_id": ObjectId(movie["_id"])})
    return "non-horror removed"



if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
