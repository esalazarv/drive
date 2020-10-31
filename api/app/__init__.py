from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Import blueprints
from app.info.routes import info
from app.users.routes import users

# Configure app
app = Flask(__name__)
app.config.from_object('app.settings.Config')
db = SQLAlchemy(app)

# Register blueprints
app.register_blueprint(info)
app.register_blueprint(users)