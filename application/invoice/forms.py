from flask_wtf import FlaskForm
from wtforms import validators, FormField
from wtforms_alchemy import ModelFieldList
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from application import db
from application.customer.models import Customer
from application.row.forms import RowForm


def get_customers():
    return Customer.query


class InvoiceForm(FlaskForm):
    customer = QuerySelectField('Customer', [validators.InputRequired(u'Please select a customer')],
                                query_factory=get_customers, get_label='name', allow_blank=True)
    rows = ModelFieldList(FormField(RowForm))

    class Meta:
        csrf = False
