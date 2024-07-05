from app.db import db
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .order_item import OrderItem


class Order(db.Model):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    customer_name = Column(String(50), nullable=False)
    customer_phone = Column(String(20), nullable=False)
    customer_address = Column(String(50), nullable=False)

    bookings = relationship('Booking', back_populates='order')
    order_items = relationship('OrderItem', back_populates='order')

    def to_dict(self):
        return {
            'order_id': self.order_id,
            'customer_name': self.customer_name,
            'customer_phone': self.customer_phone,
            'customer_address': self.customer_address,
            'items': [order_item.to_dict() for order_item in self.order_items]
        }
