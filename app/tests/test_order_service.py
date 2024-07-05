import unittest
from datetime import date
from app import create_app, db
from app.services.order_service import OrderService
from app.services.DAOs import ItemDAO
from app.tests.mock_data import create_mock_items


class OrderServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config.from_object('app.config.TestConfig')
        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()
        db.create_all()

        self.order_service = OrderService()
        self.items = create_mock_items()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.ctx.pop()

    def test_create_order_with_order_items(self):
        customer_name = 'John Doe'
        customer_phone = '1234567890'
        customer_address = '123 Main St'

        order_date = date.today()
        order_items = [
            {'item_id': self.items['White Chair'].item_id, 'quantity': 4},
            {'item_id': self.items['Long Table'].item_id, 'quantity': 2},
            {'item_id': self.items['Heaters'].item_id, 'quantity': 1},
        ]

        order = self.order_service.create_order(customer_name, customer_phone,
                                                customer_address, order_items, order_date)
        self.assertIsNotNone(order['order_id'])
        self.assertEqual(order['customer_name'], customer_name)
        self.assertEqual(order['customer_phone'], customer_phone)
        self.assertEqual(order['customer_address'], customer_address)
        self.assertEqual(len(order['order_items']), 3)
        for order_item in order['order_items']:
            item = self.items.get(next(item_name for item_name, item_obj in self.items.items()
                                       if item_obj.item_id == order_item['item_id']))
            self.assertEqual(order_item['quantity'], next(oi['quantity'] for oi in order_items
                                                          if oi['item_id'] == item.item_id))

    def test_create_order_with_insufficient_quantity(self):
        customer_name = 'Jane Doe'
        customer_phone = '0987654321'
        customer_address = '456 Elm St'
        order_date = date.today()
        order_items = [
            {'item_id': self.items['White Chair'].item_id, 'quantity': 200},  # More than available
            {'item_id': self.items['Long Table'].item_id, 'quantity': 1},
        ]

        with self.assertRaises(ValueError) as context:
            self.order_service.create_order(customer_name, customer_phone, customer_address, order_items, order_date)

        self.assertTrue('Insufficient quantities for items: White Chair' in str(context.exception))

    def test_check_in_order(self):
        # Create an order first
        customer_name = 'John Doe'
        customer_phone = '1234567890'
        customer_address = '123 Main St'
        order_date = date.today()
        order_items = [
            {'item_id': self.items['White Chair'].item_id, 'quantity': 4},
            {'item_id': self.items['Long Table'].item_id, 'quantity': 2},
            {'item_id': self.items['Heaters'].item_id, 'quantity': 1},
        ]
        order = self.order_service.create_order(customer_name, customer_phone, customer_address, order_items, order_date)

        # Check in the order
        checked_in_order = self.order_service.check_in_order(order['order_id'], order_items, order_date)

        self.assertIsNotNone(checked_in_order)
        self.assertEqual(len(checked_in_order['order_items']), 0)
        for item in order_items:
            item_record = ItemDAO.get_item_by_id(item['item_id'])
            self.assertEqual(item_record.quantity, self.items[item_record.name].quantity)


if __name__ == '__main__':
    unittest.main()