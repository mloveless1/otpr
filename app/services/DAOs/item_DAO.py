from app.models.item import Item
from app.db import db


class ItemDAO:
    @staticmethod
    def get_all_items():
        return Item.query.all()

    @staticmethod
    def get_item_by_id(item_id):
        return db.session.get(Item, item_id)

    @staticmethod
    def create_item(name, price, quantity):
        new_item = Item(name=name, price=price, quantity=quantity)
        db.session.add(new_item)
        db.session.flush()  # Ensure the ID is generated
        db.session.commit()  # Commit the transaction
        return new_item

    @staticmethod
    def update_item(item_id, name=None, price=None, quantity=None):
        item = db.session.get(Item, item_id)
        if item:
            if name:
                item.name = name
            if price:
                item.price = price
            if quantity:
                item.quantity = quantity
            db.session.commit()
        return item

    @staticmethod
    def delete_item(item_id):
        item = db.session.get(Item, item_id)
        if item:
            db.session.delete(item)
            db.session.commit()
            return True
        return False
