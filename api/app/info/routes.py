from flask import current_app, Blueprint, jsonify

info = Blueprint("api", __name__, url_prefix="/api")


@info.route("/")
def home():
    return jsonify({
        "name": current_app.config["APP_NAME"],
        "version": current_app.config["APP_VERSION"]
    })
