from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from .config import Config
from flask_mail import Mail
from celery import Celery
from .db import db

mail = Mail()
migrate = Migrate()
celery = Celery(__name__, broker=Config.CELERY_BROKER_URL)
jwt_manager = JWTManager()


def create_app() -> Flask:
    app = Flask(__name__, template_folder='../templates')

    app.config.from_object(Config)

    db.init_app(app)
    mail.init_app(app)
    jwt_manager.init_app(app)
    migrate.init_app(app, db)
    celery.conf.update(app.config)

    with app.app_context():
        # Import all models here to ensure they are registered correctly
        from .models.booking import Booking
        from .models.item import Item
        from .models.order import Order
        from .models.order_item import OrderItem

    api = Api(app)

    # Import and initialize routes
    from apis.routes import initialize_routes
    initialize_routes(api)

    return app
