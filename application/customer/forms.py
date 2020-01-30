from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class CustomerForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=3)])
    address = TextAreaField("Address")
 
    class Meta:
        csrf = False