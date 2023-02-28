from flask import request, jsonify
from flask_restful import Resource
from models import Product
from db import db


class ProductResource(Resource):
    # get individual record
    def get(self, id=None):
        pro_list = []
        if id:
            product = Product.query.get(id)
            return product.serialize()

    def put(self, id):
        print(id)
        product = Product.find_by_id(id)
        name = request.json.get('name', product.name)
        # description = request.json.get('description', product.description)
        price = request.json.get('price', product.price)
        quantity = request.json.get('quantity', product.quantity)

        product.name = name
        # product.description = description
        product.price = price
        product.quantity = quantity

        db.session.commit()

        return product.serialize()

    def delete(self, id):
        product = Product.query.get(id)
        db.session.delete(product)
        db.session.commit()

        return product.serialize()


class ProductList(Resource):
    def get(self):
        # Get all Records
        products = Product.query.all()
        print("pro...", products)
        serialized_products = [product.serialize() for product in products]
        return jsonify(serialized_products)

    def post(self):
        name = request.json['name']
        description = request.json['description']
        price = request.json['price']
        quantity = request.json['quantity']

        product = Product(name, description, price, quantity)
        db.session.add(product)
        db.session.commit()
        return product.serialize()
