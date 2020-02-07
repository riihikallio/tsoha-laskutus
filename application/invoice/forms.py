from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, validators, FormField
from wtforms_alchemy import ModelForm, ModelFieldList
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from application import db
from application.customer.models import Customer
from application.product.models import Product
from application.invoice.models import Invoice, Row

def get_customers():
    return Customer.query

def get_products():
    return Product.query

class RowForm(ModelForm):
    product = QuerySelectField('Product',[validators.InputRequired(u'Please select a product')], 
                query_factory=get_products, get_label='name', allow_blank=True)
    count = FloatField("Count", [validators.NumberRange(min=1)])

    class Meta:
        csrf = False
        model = Row


class InvoiceForm(FlaskForm):
    customer = QuerySelectField('Customer',[validators.InputRequired(u'Please select a customer')], 
                query_factory=get_customers, get_label='name', allow_blank=True)
    rows = ModelFieldList(FormField(RowForm), min_entries=1)

    class Meta:
        csrf = False