from application import db
from application.models import Base

class Product(Base):
    number = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False)
    unit = db.Column(db.String(10), nullable=False)
    price = db.Column(db.Float(), nullable=False)
    category = db.Column(db.String(144), nullable=False, index=True)

    def __init__(self, name, unit, price, category):
        self.name = name
        self.unit = unit
        self.price = price
        self.category = category