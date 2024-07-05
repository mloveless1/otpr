from marshmallow import Schema, fields


class ItemDTO:
    def __init__(self, item_id, name, price, quantity):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.quantity = quantity


class ItemSchema(Schema):
    item_id = fields.Int()
    name = fields.Str()
    price = fields.Float()
    quantity = fields.Int()
