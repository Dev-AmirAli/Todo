def Success():
    return {'message': 'item has been Created'}, 200


def NotFound():
    return {'message': 'Item not found'}, 404


def InternalError():
    return {'message': "An error occurred inserting the item."}, 500


def Deleted():
    return {'message': 'item has been deleted'}, 200


def Unauthorized(name):
    return {'message': "An item with name '{}' already exists.".format(
        name)}, 400
