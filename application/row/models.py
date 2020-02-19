from application import db

class Row(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    product_num = db.Column(db.Integer, db.ForeignKey('product.number'), nullable=False, index=True)
    product = db.relationship("Product")
    qty = db.Column(db.Integer, nullable=False)

    invoice_num = db.Column(db.Integer, db.ForeignKey('invoice.number'), nullable=False, index=True)

    def __init__(self, product, qty):
        self.product = product
        self.qty = qty

    def __str__(self):
        return "*** prod: {}, qty: {}".format(self.product.name, self.qty)