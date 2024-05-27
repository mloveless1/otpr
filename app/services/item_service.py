from app.db import db
from ..models.item import Item


class ItemService:
    def create_item(self, name, price, quantity):
        new_item = Item(name=name, price=price, quantity=quantity)
        db.session.add(new_item)
        db.session.commit()
        return new_item

    def get_item(self, item_id):
        return Item.query.get(item_id)

    def get_all_items(self):
        return Item.query.all()

    def update_item(self, item_id, name=None, price=None, quantity=None):
        item = Item.query.get(item_id)
        if not item:
            return None
        if name:
            item.name = name
        if price:
            item.price = price
        if quantity:
            item.quantity = quantity
        db.session.commit()
        return item

    def delete_item(self, item_id):
        item = Item.query.get(item_id)
        if item:
            db.session.delete(item)
            db.session.commit()
            return True
        return False
