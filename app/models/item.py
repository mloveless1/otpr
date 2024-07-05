from app.db import db
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship


class Item(db.Model):
    __tablename__ = 'items'

    item_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False)

    order_items = relationship('OrderItem', back_populates='item')

    def to_dict(self):
        return {
            'item_id': self.item_id,
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity
        }
