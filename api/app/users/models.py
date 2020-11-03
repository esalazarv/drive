from app import db
import uuid

class User(db.Model):
    id = db.Column(db.String(255), primary_key=True, default=lambda: uuid.uuid4().hex)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255))
