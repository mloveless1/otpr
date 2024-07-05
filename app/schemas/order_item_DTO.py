from marshmallow import Schema, fields


class OrderItemDTO:
    def __init__(self, id, order_id, item_id, quantity):
        self.id = id
        self.order_id = order_id
        self.item_id = item_id
        self.quantity = quantity


class OrderItemSchema(Schema):
    id = fields.Int()
    order_id = fields.Int()
    item_id = fields.Int()
    quantity = fields.Int()
