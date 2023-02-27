from flask import Blueprint
from resources.item import Item, ItemList

item_api = Blueprint('item', __name__)


@item_api.route('/<string:name>', methods=['POST'])
def CreateItem(name):
    item = Item()
    result = item.post(name)
    if result is not None:
        return result
    else:
        return None


@item_api.route('/<string:name>', methods=['GET'])
def GetItemByName(name):
    item = Item()
    result = item.get(name)
    if result is not None:
        return result
    else:
        return None


@item_api.route('/<string:name>', methods=['PUT'])
def UpdateItemByName(name):
    item = Item()
    result = item.put(name)
    if result is not None:
        return result
    else:
        return None


@item_api.route('/<string:name>', methods=['DELETE'])
def DeleteItemByName(name):
    item = Item()
    result = item.delete(name)
    if result is not None:
        return result
    else:
        return None


@item_api.route('/items/', methods=['GET'])
def GetItem():
    item = ItemList()
    result = item.get()
    if result is not None:
        return result
    else:
        return None
