from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms_alchemy import ModelForm
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from application.row.models import Row
from application.product.models import Product


def get_products():
    return Product.query


class RowForm(FlaskForm, ModelForm):
    product = QuerySelectField('Product', query_factory=get_products, get_label='name', allow_blank=True)
    qty = StringField("Qty")

    class Meta:
        csrf = False
        model = Row
