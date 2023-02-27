""" Todo Flask App """
from flask import Flask
from flask_jwt_extended import JWTManager
from flask_restful import Api
from routes.user import user_api
from config import MSQL_CONFIG
from db import db

app = Flask(__name__)

app.register_blueprint(user_api, url_prefix='/user')

app.config['SQLALCHEMY_DATABASE_URI'] = MSQL_CONFIG
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)
api = Api(app)


@app.before_first_request
def create_tables():
    """To Create Table in Database"""
    db.init_app(app)
    db.create_all()


if __name__ == '__main__':
    app.run(debug=True)  # important to mention debug=True
