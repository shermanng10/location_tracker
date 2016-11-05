import os

class Config(object):
    DEBUG = False
    TESTING = False


class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE='location_api.db'
    SECRET_KEY='development key'
    USERNAME='admin'
    PASSWORD='default'

class TestingConfig(Config):
    TESTING = True
    LOGGER_HANDLER_POLICY = 'never'
