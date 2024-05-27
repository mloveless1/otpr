from flask_restful import Resource
from flask import request, jsonify
from app.services.booking_service import BookingService


class BookingResource(Resource):
    def __init__(self):
        self.booking_service = BookingService()

    def post(self):
        data = request.get_json()
        start_date = data.get('start_date')
        end_date = data.get('end_date')
        customer_name = data.get('customer_name')
        customer_phone = data.get('customer_phone')
        customer_address = data.get('customer_address')
        item_quantities = data.get('item_quantities')

        try:
            new_booking = self.booking_service.create_booking(
                start_date, end_date, customer_name, customer_phone, customer_address, item_quantities
            )
            return jsonify(new_booking.to_dict())
        except ValueError as e:
            return {'error': str(e)}, 400

    def get(self, booking_id):
        booking = self.booking_service.get_booking(booking_id)
        if booking:
            return jsonify(booking.to_dict())
        return {'error': 'Booking not found'}, 404
