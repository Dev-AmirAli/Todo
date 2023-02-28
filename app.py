from flask import Flask
from flask_restful import Api
from db import db
from resource import ProductResource,ProductList
from routes import product_api
app = Flask(__name__)
api = Api(app)


app.register_blueprint(product_api)
# database MySQL config
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:root@localhost:3306/mydb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


@app.before_first_request
def create_tables():
    """To Create Table in Database"""
    db.init_app(app)
    db.create_all()


# Database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# api.add_resource(ProductList, '/products')
# api.add_resource(ProductResource, '/product/<int:id>')
if __name__ == '__main__':
    app.run(debug=True)
