from flask import Blueprint
from resources.store import Store, StoreList

store_api = Blueprint('store', __name__)


@store_api.route('/<string:name>', methods=['POST'])
def CreateStore(name):
    store = Store()
    result = store.post(name)
    if result is not None:
        return result
    else:
        return None


@store_api.route('/<string:name>', methods=['GET'])
def GetStoreByName(name):
    store = Store()
    result = store.get(name)
    if result is not None:
        return result
    else:
        return None


@store_api.route('/<string:name>', methods=['DELETE'])
def DeleteStoreByName(name):
    store = Store()
    result = store.delete(name)
    if result is not None:
        return result
    else:
        return None


@store_api.route('/stores/', methods=['GET'])
def GetStore():
    store = StoreList()
    result = store.get()
    if result is not None:
        return result
    else:
        return None
