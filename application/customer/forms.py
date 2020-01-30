from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField

class CustomerForm(FlaskForm):
    name = StringField("Name")
    address = TextAreaField("Address")
 
    class Meta:
        csrf = False