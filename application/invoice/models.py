from flask_login import current_user
from application import db

class Invoice(db.Model):
    number = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    customer_num = db.Column(db.Integer, db.ForeignKey('customer.number'), nullable=False)
    customer = db.relationship("Customer")
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    rows = db.relationship("Row", backref="invoice", cascade="delete")

    def __init__(self, customer, rows):
        self.customer = customer
        self.rows = rows
        self.account_id = current_user.id
