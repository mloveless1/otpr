from app.models.order_item import OrderItem
from app.db import db


class OrderItemDAO:

    def _get_order_item_by_id(self, order_item_id):
        return db.session.get(OrderItem, order_item_id)

    def _commit(self):
        db.session.flush()  # Ensure the ID is generated
        db.session.commit()  # Commit the transaction

    def get_all_order_items(self):
        return OrderItem.query.all()

    def get_order_item_by_id(self, order_item_id):
        return self._get_order_item_by_id(order_item_id)

    def get_order_item_by_order_and_item(self, order_id, item_id):
        return OrderItem.query.filter_by(order_id=order_id, item_id=item_id).first()

    def create_order_item(self, order_id, item_id, quantity):
        new_order_item = OrderItem(order_id=order_id, item_id=item_id, quantity=quantity)
        db.session.add(new_order_item)
        self._commit()
        return new_order_item

    def update_order_item(self, order_item_id, order_id=None, item_id=None, quantity=None):
        order_item = self._get_order_item_by_id(order_item_id)
        if not order_item:
            raise ValueError(f"Order item with id {order_item_id} not found")

        if order_id is not None:
            order_item.order_id = order_id
        if item_id is not None:
            order_item.item_id = item_id
        if quantity is not None:
            order_item.quantity = quantity

        self._commit()
        return order_item

    def delete_order_item(self, order_item_id):
        order_item = self._get_order_item_by_id(order_item_id)
        if not order_item:
            raise ValueError(f"Order item with id {order_item_id} not found")

        db.session.delete(order_item)
        self._commit()
        return True
