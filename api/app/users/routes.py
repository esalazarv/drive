from flask import Blueprint, jsonify
from app.users.models import User

users = Blueprint("users", __name__, url_prefix="/api/users")


@users.route("/")
def index():
    return jsonify({
        "data": []
    })
