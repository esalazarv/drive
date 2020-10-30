from flask import Flask
from app.settings import config
app = Flask(__name__)

@app.route("/")
def hello_world():
    return config.get("app.name") + " works!"