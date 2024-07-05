from app.db import db
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship


class OrderItem(db.Model):
    __tablename__ = 'order_items'

    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    order_id = Column(Integer, ForeignKey('orders.order_id'), nullable=False)
    item_id = Column(Integer, ForeignKey('items.item_id'), nullable=False)
    quantity = Column(Integer, nullable=False)

    order = relationship('Order', back_populates='order_items')
    item = relationship('Item')

    def to_dict(self):
        return {
            'id': self.id,
            'order_id': self.order_id,
            'item_id': self.item_id,
            'quantity': self.quantity,
        }
