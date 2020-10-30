from flask import Flask

# Import blueprints
from app.info.routes import info
from app.users.routes import users

# Configure app
app = Flask(__name__)
app.register_blueprint(info)
app.register_blueprint(users)