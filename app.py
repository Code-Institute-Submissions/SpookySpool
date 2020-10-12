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
    movies = mongo.db.movies.find({"year": {"$gte": "1990"}})
    count = 0
    for movie in movies:
        count += 1
    print(count) 

    return "There are " + str(count)


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
