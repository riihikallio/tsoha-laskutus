from flask_login import current_user
from application import db
from application.models import Base

class Invoice(Base):
    number = db.Column(db.Integer, primary_key=True)
    customer_num = db.Column(db.Integer, db.ForeignKey('customer.number'), nullable=False, index=True)
    customer = db.relationship("Customer")
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False, index=True)

    rows = db.relationship("Row", backref="invoice", cascade="delete")

    def __init__(self, customer, rows):
        self.customer = customer
        self.rows = rows
        self.account_id = current_user.id
