from app.services.DAOs import ItemDAO


def create_mock_items():
    items = [
        {'name': 'White Chair', 'price': 10.0, 'quantity': 100},
        {'name': 'Kid Chair', 'price': 8.0, 'quantity': 100},
        {'name': 'Long Table', 'price': 20.0, 'quantity': 50},
        {'name': 'Round Table', 'price': 15.0, 'quantity': 50},
        {'name': 'Heaters', 'price': 50.0, 'quantity': 20},
        {'name': '20x20 Tent', 'price': 200.0, 'quantity': 10},
        {'name': '20x30 Tent', 'price': 300.0, 'quantity': 10},
    ]
    created_items = {item['name']: ItemDAO.create_item(**item) for item in items}

    # Debugging: Print out item IDs to ensure they are generated correctly
    for name, item in created_items.items():
        print(f"Item created: {name}, ID: {item.item_id}")

    return created_items

def create_mock_customer():
    customer = {
        'name': 'John',
        'address': '123 Main Street',
        'email': 'email@example.com',
        'phone': '+9112345678'

    }

    return customer