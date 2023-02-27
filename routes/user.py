
from flask import Blueprint
from resources.user import User, UserRegister

user_api = Blueprint('user', __name__)


@user_api.route('/register', methods=['POST'])
def CreateUser():
    user = UserRegister()
    result = user.post()
    if result is not None:
        return result
    else:
        return None


@user_api.route('/login', methods=['GET'])
def GetUser():
    user = User()
    result = user.post()
    if result is not None:
        return result
    else:
        return None
