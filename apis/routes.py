from flask_restful import Api
from .booking_api import BookingResource
from .item_api import ItemResource
from .item_api import ItemListResource


def initialize_routes(api):
    api.add_resource(BookingResource, '/booking', '/booking/<int:booking_id>')
    api.add_resource(ItemResource, '/item/<int:item_id>')
    api.add_resource(ItemListResource, '/items')