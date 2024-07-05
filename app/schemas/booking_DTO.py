from marshmallow import Schema, fields


class BookingDTO:
    def __init__(self, booking_id, start_date, end_date, order_id):
        self.booking_id = booking_id
        self.start_date = start_date
        self.end_date = end_date
        self.order_id = order_id


class BookingSchema(Schema):
    booking_id = fields.Int()
    start_date = fields.Date()
    end_date = fields.Date()
    order_id = fields.Int()
