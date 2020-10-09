import os
from flask import Flask
from flask_pymongo import PyMongo

app = Flask(__name__)

app.config["MONGO_DBNAME"] = "spooky_spool"
app.config["MONGO_URI"] = os.getenv("MONGODB_URI")

mongo = PyMongo(app)


@app.route("/")
def index():
    return "flask is connected"


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
