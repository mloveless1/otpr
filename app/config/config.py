import os


class Config:
    CELERY_BROKER_URL = os.getenv('REDIS_URL')
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    NOTIFICATION_EMAIL_RECEIVERS = ''
    NOTIFICATION_EMAIL_SENDER = ''
    MAIL_PASSWORD = ''
    MAIL_SERVER = ''
    MAIL_PORT = ''
    REDIS_URL = os.getenv('REDIS_URL')
    USERNAME_TOKEN = ''


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'  # In-memory database for testing
    SQLALCHEMY_ECHO = False