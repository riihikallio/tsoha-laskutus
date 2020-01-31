from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators, ValidationError
from application.auth.models import User
  
class LoginForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=3)])
    password = PasswordField("Password", [validators.Length(min=3)])

    def validate_username(form, field):
        if User.query.filter_by(username=form.username.data).first():
            raise ValidationError('Username already in use')
  
    class Meta:
        csrf = False