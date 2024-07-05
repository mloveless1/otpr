from app.services.DAOs import ItemDAO
from app.schemas.item_DTO import ItemSchema


class ItemService:
    def __init__(self):
        self.item_dao = ItemDAO()
        self.item_schema = ItemSchema()

    def get_all_items(self):
        items = ItemDAO.get_all_items()
        return [self.item_schema.dump(item) for item in items]

    def get_item_by_id(self, item_id):
        item = ItemDAO.get_item_by_id(item_id)
        if item:
            return self.item_schema.dump(item)
        return None

    def create_item(self, name, price, quantity):
        new_item = ItemDAO.create_item(name, price, quantity)
        return self.item_schema.dump(new_item)

    def update_item(self, item_id, name=None, price=None, quantity=None):
        updated_item = ItemDAO.update_item(item_id, name, price, quantity)
        if updated_item:
            return self.item_schema.dump(updated_item)
        return None

    def delete_item(self, item_id):
        return self.item_dao.delete_item(item_id)
