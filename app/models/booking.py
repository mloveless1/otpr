from app.db import db
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship


class Booking(db.Model):
    __tablename__ = 'bookings'

    booking_id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    start_date = Column(DateTime)
    end_date = Column(DateTime)
    order_id = Column(Integer, ForeignKey('orders.order_id'))

    order = relationship("Order", back_populates="bookings")

    def to_dict(self):
        return {
            'booking_id': self.booking_id,
            'start_date': self.start_date.isoformat(),
            'end_date': self.end_date.isoformat(),
            'order_id': self.order_id,
        }