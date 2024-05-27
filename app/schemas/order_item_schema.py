from marshmallow import Schema, fields
from .item_schema import ItemSchema


class OrderItemSchema(Schema):
    order_id = fields.Int()
    item_id = fields.Int()
    quantity = fields.Int()
    item = fields.Nested(ItemSchema())
