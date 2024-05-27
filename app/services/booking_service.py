from app.db import db
from app.models.booking import Booking
from app.models.order import Order
from app.models.order_item import OrderItem
from app.models.item import Item


class BookingService:
    def create_booking(self, start_date, end_date, customer_name, customer_phone, customer_address, item_quantities):
        try:
            # Start a new transaction
            new_order = Order(
                customer_name=customer_name,
                customer_phone=customer_phone,
                customer_address=customer_address
            )
            db.session.add(new_order)
            db.session.flush()  # Flush to get new_order.order_id

            # Create order items and update quantities
            for item_id, quantity in item_quantities.items():
                item = Item.query.get(item_id)
                if item and item.quantity >= quantity:
                    order_item = OrderItem(
                        order_id=new_order.order_id,
                        item_id=item_id,
                        quantity=quantity
                    )
                    db.session.add(order_item)
                    item.quantity -= quantity  # Update item quantity
                else:
                    raise ValueError(f"Item {item_id} not available in the requested quantity")

            # Create a new booking
            new_booking = Booking(
                start_date=start_date,
                end_date=end_date,
                order_id=new_order.order_id
            )
            db.session.add(new_booking)

            # Commit the transaction only if all operations succeed
            db.session.commit()

            return new_booking

        except Exception as e:
            # Rollback the transaction if any error occurs
            db.session.rollback()
            raise e

    def get_booking(self, booking_id):
        return Booking.query.get(booking_id)
