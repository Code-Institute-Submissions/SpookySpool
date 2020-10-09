import os
import json
from flask import Flask
from flask_pymongo import PyMongo

if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "spooky_spool"
app.config["MONGO_URI"] = os.getenv("MONGODB_URI")

mongo = PyMongo(app)

data = []
with open("data/movie.json", "r") as json_data:
    data = json.load(json_data)
test = {"title": "Test insert"}

@app.route("/")
def index():
    mongo.db.movies.insert_many(data)
    return "flask is connected"


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
