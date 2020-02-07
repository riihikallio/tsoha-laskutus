from application import db

class Invoice(db.Model):
    number = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    customer_num = db.Column(db.Integer, db.ForeignKey('customer.number'), nullable=False)
    customer = db.relationship("Customer")
    account_id = db.Column(db.Integer, db.ForeignKey('account.id'), nullable=False)

    rows = db.relationship("Row", backref="invoice")

    def __init__(self, customer, rows):
        self.customer = customer
        self.rows = rows
        self.account_id = current_user.id


class Row(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    product_num = db.Column(db.Integer, db.ForeignKey('product.number'), nullable=False)
    product = db.relationship("Product")
    count = db.Column(db.Integer, nullable=False)

    invoice_num = db.Column(db.Integer, db.ForeignKey('invoice.number'), nullable=False)

    def __init__(self, product, count):
        self.product = product
        self.count = count

