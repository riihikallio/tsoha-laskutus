from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, validators

class ProductForm(FlaskForm):
    name = StringField("Name", [validators.Length(min=3,max=144)])
    unit = StringField("Unit", [validators.Length(min=1,max=10)])
    price = FloatField("Price", [validators.NumberRange(min=0.01)])
    category = SelectField("Category", \
        choices=[('Laitteet', 'Laitteet'), ('Osat', 'Osat'), ('Palvelut', 'Palvelut')], \
            validators=[validators.Required(message='Category is required')])

    class Meta:
        csrf = False