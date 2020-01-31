from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, validators

class ProductForm(FlaskForm):
    name = StringField("Name", [validators.InputRequired()])
    unit = StringField("Unit", [validators.InputRequired()])
    price = FloatField("Price", [validators.NumberRange(min=0.01)])
    category = StringField("Category", [validators.InputRequired()])

    class Meta:
        csrf = False