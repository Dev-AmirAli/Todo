from flask import Blueprint
from resource import ProductResource, ProductList

product_api = Blueprint('product', __name__)


@product_api.route('/product', methods=['POST'])
def CreateProduct():
    product = ProductList()
    result = product.post()
    if result is not None:
        return result
    else:
        return None

@product_api.route('/product/<int:id>', methods=['GET'])
def FetchProductById(id):
    product = ProductResource()
    result = product.get(id)
    if result is not None:
        return result
    else:
        return None

@product_api.route('/products', methods=['GET'])
def FetchProduct():
    product = ProductList()
    result = product.get()
    if result is not None:
        return result
    else:
        return None


@product_api.route('/product/<int:id>', methods=['PUT'])
def GetProductByID(id):
    product = ProductResource()
    result = product.put(id)
    if result is not None:
        return result
    else:
        return None


@product_api.route('/product/<int:id>', methods=['DELETE'])
def DeleteProductByID(id):
    product = ProductResource()
    result = product.delete(id)
    if result is not None:
        return result
    else:
        return None
