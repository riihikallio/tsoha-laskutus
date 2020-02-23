from application import db
from application.models import Base


class Customer(Base):
    number = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(144), nullable=False, index=True)
    address = db.Column(db.String(255))

    def __init__(self, name, address):
        self.name = name
        self.address = address
