from movier.data.models import db
import os


class BaseConfig(object):
    DEBUG = False
    TESTING = False
    # sqlite :memory: identifier is the default if no filepath is present
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movie_db.db'
    SECRET_KEY = '1d94e52c-1c89-4515-b87a-f48cf3cb7f0b'


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///movie_db.db'
    SECRET_KEY = 'a9eec0e0-23b7-4788-9a92-318347b9a39f'


class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
    SECRET_KEY = '792842bc-c4df-4de1-9177-d5207bd9faa6'

config = {
    "development": "movier.config.DevelopmentConfig",
    "testing": "movier.config.TestingConfig",
    "default": "movier.config.DevelopmentConfig"
}


def configure_application(application):
    config_name = os.getenv('FLASK_CONFIGURATION', 'default')
    application.config.from_object(config[config_name])

