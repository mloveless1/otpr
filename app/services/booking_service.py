from datetime import datetime

from app.services.DAOs.booking_DAO import BookingDAO
from app.schemas.booking_DTO import BookingSchema


class BookingService:
    def __init__(self):
        self.booking_schema = BookingSchema()
        self.booking_dao = BookingDAO()

    def get_all_bookings(self):
        bookings = BookingDAO.get_all_bookings()
        return [self.booking_schema.dump(booking) for booking in bookings]

    def get_booking(self, booking_id):
        booking = BookingDAO.get_booking_by_id(booking_id)
        if booking:
            return self.booking_schema.dump(booking)
        return None

    def create_booking(self, start_date, end_date, order_id):
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
        end_date = datetime.strptime(end_date, "%Y-%m-%d")
        new_booking = BookingDAO.create_booking(start_date, end_date, order_id)
        return self.booking_schema.dump(new_booking)

    def update_booking(self, booking_id, start_date=None, end_date=None, order_id=None):
        updated_booking = BookingDAO.update_booking(booking_id, start_date, end_date, order_id)
        if updated_booking:
            return self.booking_schema.dump(updated_booking)
        return None

    def delete_booking(self, booking_id):
        return self.booking_dao.delete_booking(booking_id)
