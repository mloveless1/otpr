from app.models.order import Order
from app.db import db


class OrderDAO:
    @staticmethod
    def get_all_orders():
        return Order.query.all()

    @staticmethod
    def get_order_by_id(order_id):
        return db.session.get(Order, order_id)

    @staticmethod
    def create_order(customer_name, customer_phone, customer_address):
        new_order = Order(customer_name=customer_name, customer_phone=customer_phone, customer_address=customer_address)
        db.session.add(new_order)
        db.session.flush()
        db.session.commit()
        return new_order

    @staticmethod
    def update_order(order_id, customer_name=None, customer_phone=None, customer_address=None):
        order = db.session.get(Order, order_id)
        if order:
            if customer_name:
                order.customer_name = customer_name
            if customer_phone:
                order.customer_phone = customer_phone
            if customer_address:
                order.customer_address = customer_address
            db.session.commit()
        return order

    @staticmethod
    def delete_order(order_id):
        order = db.session.get(Order, order_id)
        if order:
            db.session.delete(order)
            db.session.commit()
            return True
        return False
