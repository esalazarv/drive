from flask import Blueprint, jsonify

users = Blueprint("users", __name__, url_prefix="/api/users")


@users.route("/")
def index():
    return jsonify({
        "data": []
    })
