from app.db import db
from sqlalchemy import Column, Integer, ForeignKey


class OrderItem(db.Model):
    __tablename__ = 'order_items'

    order_id = Column(Integer, ForeignKey('orders.order_id'), primary_key=True)
    item_id = Column(Integer, ForeignKey('items.item_id'), primary_key=True)
    quantity = Column(Integer, nullable=False, default=1)

    order = db.relationship('Order', back_populates='order_items')
    item = db.relationship('Item', back_populates='order_items')

    def to_dict(self):
        return {
            'order_id': self.order_id,
            'item_id': self.item_id,
            'quantity': self.quantity,
            'item': self.item.to_dict()
        }
