from db import db


class Product(db.Model):
    # db.Column(db.String(100), unique=True)
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    # description = db.Column(db.String(200))
    price = db.Column(db.Float)
    quantity = db.Column(db.Integer)
    # products = db.relationship('ProductModel', lazy='dynamic')

    def __init__(self, name, description, price, quantity):
        self.name = name
        # self.description = description
        self.price = price
        self.quantity = quantity

    def serialize(self):
        # print(f"Serializing product with id {self.id}")
        return {
            'id': self.id,
            'name': self.name,
            # 'description': self.description,
            'price': float(self.price),
        }

    @classmethod
    def find_by_id(cls, id):
        query = cls.query.filter(cls.id == id).first()
        return query





