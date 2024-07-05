from app.services.DAOs import OrderDAO
from app.services.DAOs import OrderItemDAO
from app.services.DAOs import ItemDAO
from app.utils import ItemQuantitiesCache
from app.schemas.order_DTO import OrderSchema
from app.db import db


class OrderService:
    def __init__(self):
        self.order_schema = OrderSchema()
        self.order_item_dao = OrderItemDAO()
        self.order_dao = OrderDAO()
        self.item_quantity_cache = ItemQuantitiesCache()

    def get_all_orders(self):
        orders = OrderDAO.get_all_orders()
        return [self.order_schema.dump(order) for order in orders]

    def get_order(self, order_id):
        order = OrderDAO.get_order_by_id(order_id)
        if order:
            return self.order_schema.dump(order)
        return None

    def _initialize_cache(self, order_items, order_date):
        for item in order_items:
            if self.item_quantity_cache.get_quantity(item['item_id'], order_date) is None:
                item_record = ItemDAO.get_item_by_id(item['item_id'])
                self.item_quantity_cache.set_quantity(item['item_id'], order_date, item_record.quantity)

    def _check_item_quantities(self, order_items, order_date):
        insufficient_items = []
        for item in order_items:
            available_quantity = self.item_quantity_cache.get_quantity(item['item_id'], order_date)
            if available_quantity < item['quantity']:
                item_record = ItemDAO.get_item_by_id(item['item_id'])
                insufficient_items.append(item_record.name)
        if insufficient_items:
            raise ValueError(f"Insufficient quantities for items: {', '.join(insufficient_items)}")

    def _update_item_quantities(self, order_items, order_date):
        for item in order_items:
            self.item_quantity_cache.update_quantity(item['item_id'], order_date, -item['quantity'])

    def _restore_item_quantities(self, order_items, order_date):
        for item in order_items:
            self.item_quantity_cache.update_quantity(item['item_id'], order_date, item['quantity'])

    def _delete_order_items(self, order_id, order_items):
        for item in order_items:
            order_item = self.order_item_dao.get_order_item_by_order_and_item(order_id, item['item_id'])
            if order_item:
                self.order_item_dao.delete_order_item(order_item.id)

    def create_order(self, customer_name, customer_phone, customer_address, order_items, order_date):
        self._initialize_cache(order_items, order_date)
        self._check_item_quantities(order_items, order_date)

        new_order = OrderDAO.create_order(customer_name, customer_phone, customer_address)
        for item in order_items:
            self.order_item_dao.create_order_item(new_order.order_id, item['item_id'], item['quantity'])
        self._update_item_quantities(order_items, order_date)
        db.session.commit()

        return self.get_order(new_order.order_id)

    def update_order(self, order_id, customer_name=None, customer_phone=None, customer_address=None):
        updated_order = OrderDAO.update_order(order_id, customer_name, customer_phone, customer_address)
        if updated_order:
            return self.order_schema.dump(updated_order)
        return None

    def delete_order(self, order_id):
        return self.order_dao.delete_order(order_id)

    def check_in_order(self, order_id, order_items, order_date):
        order = OrderDAO.get_order_by_id(order_id)

        if not order:
            raise ValueError("Order not found")

        self._restore_item_quantities(order_items, order_date)
        self._delete_order_items(order_id, order_items)
        db.session.commit()

        return self.get_order(order_id)