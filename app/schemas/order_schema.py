from marshmallow import Schema, fields
from .order_item_schema import OrderItemSchema


class OrderSchema(Schema):
    order_id = fields.Int()
    customer_name = fields.Str()
    customer_phone = fields.Str()
    customer_address = fields.Str()
    order_items = fields.List(fields.Nested(OrderItemSchema()))
