from flask import request, jsonify
from flask_restful import Resource
from app.services.item_service import ItemService


class ItemResource(Resource):
    def __init__(self):
        self.item_service = ItemService()

    def post(self):
        data = request.get_json()
        name = data.get('name')
        price = data.get('price')
        quantity = data.get('quantity')
        new_item = self.item_service.create_item(name, price, quantity)
        return jsonify(new_item.to_dict())

    def get(self, item_id):
        item = self.item_service.get_item(item_id)
        if item:
            return jsonify(item.to_dict())
        return {'error': 'Item not found'}, 404


class ItemListResource(Resource):
    def __init__(self):
        self.item_service = ItemService()

    def get(self):
        items = self.item_service.get_all_items()
        return jsonify([item.to_dict() for item in items])

    def put(self, item_id):
        data = request.get_json()
        name = data.get('name')
        price = data.get('price')
        quantity = data.get('quantity')
        updated_item = self.item_service.update_item(item_id, name, price, quantity)
        if updated_item:
            return jsonify(updated_item.to_dict())
        return {'error': 'Item not found'}, 404

    def delete(self, item_id):
        success = self.item_service.delete_item(item_id)
        if success:
            return {'message': 'Item deleted successfully'}
        return {'error': 'Item not found'}, 404
