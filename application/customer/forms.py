from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, validators

class CustomerForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=3,max=144)])
    address = TextAreaField("Address", [validators.Length(min=3,max=255)])
 
    class Meta:
        csrf = False