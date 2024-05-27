from marshmallow import Schema, fields


class ItemSchema(Schema):
    item_id = fields.Int()
    name = fields.Str()
    price = fields.Float()
    quantity = fields.Int()