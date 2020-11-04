from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.validators import DataRequired, EqualTo
from core.validators import Unique
from app.users.models import User

class SignUpForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Unique(User, User.username)])
    password = PasswordField('password', validators=[DataRequired()])
    password_confirmation = PasswordField('password_confirmation', validators=[EqualTo('password')])