import unittest
from app import create_app, db
from app.services.booking_service import BookingService
from app.models.order import Order


class BookingServiceTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app.config.from_object('app.config.TestConfig')
        self.client = self.app.test_client()
        self.ctx = self.app.app_context()
        self.ctx.push()
        db.create_all()

        self.booking_service = BookingService()

        # Add a sample order to use for booking
        order = Order(customer_name='John Doe', customer_phone='1234567890', customer_address='123 Main St')
        db.session.add(order)
        db.session.commit()
        self.order_id = order.order_id

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.ctx.pop()

    def test_create_booking(self):
        start_date = '2024-01-01'
        end_date = '2024-01-10'

        booking = self.booking_service.create_booking(start_date, end_date, self.order_id)
        self.assertIsNotNone(booking['booking_id'])
        self.assertEqual(booking['start_date'], start_date)
        self.assertEqual(booking['end_date'], end_date)
        self.assertEqual(booking['order_id'], self.order_id)

    def test_get_booking(self):
        start_date = '2024-01-01'
        end_date = '2024-01-10'

        booking = self.booking_service.create_booking(start_date, end_date, self.order_id)
        fetched_booking = self.booking_service.get_booking(booking['booking_id'])
        self.assertIsNotNone(fetched_booking)
        self.assertEqual(fetched_booking['booking_id'], booking['booking_id'])
        self.assertEqual(fetched_booking['start_date'], booking['start_date'])
        self.assertEqual(fetched_booking['end_date'], booking['end_date'])
        self.assertEqual(fetched_booking['order_id'], booking['order_id'])


if __name__ == '__main__':
    unittest.main()
