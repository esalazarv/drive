import datetime
import uuid
from app import db

class User(db.Model):
    id = db.Column(db.String(255), primary_key=True, default=lambda: uuid.uuid4().hex)
    username = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, default=lambda: datetime.datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=lambda: datetime.datetime.utcnow)
