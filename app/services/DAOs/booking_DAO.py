from app.models.booking import Booking
from app.db import db


class BookingDAO:
    @staticmethod
    def get_all_bookings():
        return Booking.query.all()

    @staticmethod
    def get_booking_by_id(booking_id):
        return db.session.get(Booking, booking_id)

    @staticmethod
    def create_booking(start_date, end_date, order_id):
        new_booking = Booking(start_date=start_date, end_date=end_date, order_id=order_id)
        db.session.add(new_booking)
        db.session.flush()
        db.session.commit()
        return new_booking

    @staticmethod
    def update_booking(booking_id, start_date=None, end_date=None, order_id=None):
        booking = db.session.get(Booking, booking_id)
        if booking:
            if start_date:
                booking.start_date = start_date
            if end_date:
                booking.end_date = end_date
            if order_id:
                booking.order_id = order_id
            db.session.commit()
        return booking

    @staticmethod
    def delete_booking(booking_id):
        booking = db.session.get(Booking, booking_id)
        if booking:
            db.session.delete(booking)
            db.session.commit()
            return True
        return False
