from flask import Blueprint, jsonify
from app.settings import config

info = Blueprint("api", __name__, url_prefix="/api")


@info.route("/")
def home():
    return jsonify({
        "name": config.get("app.name"),
        "version": config.get("app.version")
    })
