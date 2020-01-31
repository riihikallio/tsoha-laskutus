from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, validators

class ProductForm(FlaskForm):
    name = StringField("Name", [validators.InputRequired()])
    unit = StringField("Unit", [validators.InputRequired()])
    price = FloatField("Price", [validators.NumberRange(min=0.01)])
    category = SelectField("Category", choices=[('Laitteet', 'Laitteet'), ('Osat', 'Osat'), ('Palvelut', 'Palvelut')])

    class Meta:
        csrf = False