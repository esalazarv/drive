from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()
migrate = Migrate()

def application():
    # Configure app
    app = Flask(__name__)
    app.config.from_object('app.settings.Config')
    db.init_app(app)
    migrate.init_app(app, db)

    # Import blueprints
    from app.info.routes import info
    app.register_blueprint(info)

    from app.users.routes import users
    app.register_blueprint(users)
    
    return app