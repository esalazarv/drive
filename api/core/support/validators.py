from app import db
from wtforms import ValidationError

class Unique(object):
    def __init__(self, model, field, message=None):
        self.model = model
        self.field = field
        self.message = message

    def __call__(self, form, field):
        # Check if exists a record with the same vale for a field
        exist = bool(self.model.query.filter(self.field == field.data).first())
        # If exists then raise an error
        if exist:
            # Set a message if was not defined 
            message = self.message if self.message is not None else "Value already taken."
            raise ValidationError(message)