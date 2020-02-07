from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, validators
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from application.customer.models import Customer

def get_customers():
    return Customer.query

class InvoiceForm(FlaskForm):
    customer = QuerySelectField('Customer',[validators.InputRequired(u'Please select a customer')], 
                query_factory=get_customers, get_label='name', allow_blank=True)

    class Meta:
        csrf = False