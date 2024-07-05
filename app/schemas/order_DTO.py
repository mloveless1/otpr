from marshmallow import Schema, fields
from .order_item_DTO import OrderItemSchema

class OrderDTO:
    def __init__(self, order_id, customer_name, customer_phone, customer_address, order_items):
        self.order_id = order_id
        self.customer_name = customer_name
        self.customer_phone = customer_phone
        self.customer_address = customer_address
        self.order_items = order_items


class OrderSchema(Schema):
    order_id = fields.Int()
    customer_name = fields.Str()
    customer_phone = fields.Str()
    customer_address = fields.Str()
    order_items = fields.List(fields.Nested(OrderItemSchema()))