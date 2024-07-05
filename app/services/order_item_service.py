from app.services.DAOs.order_item_DAO import OrderItemDAO
from app.schemas.order_item_DTO import OrderItemSchema


# noinspection PyArgumentList
class OrderItemService:
    def __init__(self):
        self.order_item_schema = OrderItemSchema()
        self.order_item_dao = OrderItemDAO()

    def get_all_order_items(self):
        order_items = OrderItemDAO.get_all_order_items()
        return [self.order_item_schema.dump(order_item) for order_item in order_items]

    def get_order_item(self, order_item_id):
        order_item = OrderItemDAO.get_order_item_by_id(order_item_id)
        if order_item:
            return self.order_item_schema.dump(order_item)
        return None

    def create_order_item(self, order_id, item_id, quantity):
        new_order_item = OrderItemDAO.create_order_item(order_id, item_id, quantity)
        return self.order_item_schema.dump(new_order_item)

    def update_order_item(self, order_item_id, order_id=None, item_id=None, quantity=None):
        updated_order_item = OrderItemDAO.update_order_item(order_item_id, order_id, item_id, quantity)
        if updated_order_item:
            return self.order_item_schema.dump(updated_order_item)
        return None

    def delete_order_item(self, order_item_id):
        return self.order_item_dao.delete_order_item(order_item_id)
