from flask import Blueprint, jsonify, request
from app import db
from app.users.models import User
from app.auth.forms import SignUpForm

auth = Blueprint("auth", __name__, url_prefix="/api/auth")

@auth.route("/signup", methods=["POST"])
def sign_up():
    form = SignUpForm()
    if not form.validate():
        response = jsonify({
            "error": "unprocessable entity",
            "fields": dict(form.errors.items())
        })
        response.status_code = 422
        return response
    username = request.form.get("username")
    password = request.form.get("password")
    user = User(username=username, password=password)
    db.session.add(user)
    db.session.commit()
    return jsonify({
        "data": {
            "username": username, 
            "password": password
        }
    })