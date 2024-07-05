import redis
import json
from datetime import timedelta


# TODO switch hardcoded creds with env variables
class ItemQuantitiesCache:
    def __init__(self, host='localhost', port=6379, db=0):
        self.client = redis.Redis(host=host, port=port, db=db)

    def get_quantity(self, item_id, order_date):
        key = f"item_quantity:{order_date}:{item_id}"
        value = self.client.get(key)
        return int(str(value)) if value else None

    def set_quantity(self, item_id, order_date, quantity, expiration_days=7):
        key = f"item_quantity:{order_date}:{item_id}"
        self.client.setex(key, timedelta(days=expiration_days), quantity)

    def update_quantity(self, item_id, order_date, quantity_change, expiration_days=7):
        key = f"item_quantity:{order_date}:{item_id}"
        current_quantity = self.get_quantity(item_id, order_date)
        if current_quantity is None:
            current_quantity = 0
        new_quantity = current_quantity + quantity_change
        self.set_quantity(item_id, order_date, new_quantity, expiration_days)
