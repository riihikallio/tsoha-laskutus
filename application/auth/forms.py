from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators, ValidationError
from application.auth.models import User
  
class LoginForm(FlaskForm):
    username = StringField("Username", [validators.Length(min=3,max=144)])
    password = PasswordField("Password", [validators.Length(min=3,max=144)])

    def validate_username(form, field):
        if not User.query.filter_by(username=form.username.data).count()==0:
            raise ValidationError('Username already in use')
  
    class Meta:
        csrf = False