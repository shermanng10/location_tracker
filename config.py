class Config(object):
    DEBUG = False
    TESTING = False
    DATABASE = 'location_api.db'
    SECRET_KEY = 'development key'
    USERNAME = 'admin'
    PASSWORD = 'default'
    ICLOUD_USER = 'usernamehere'
    ICLOUD_PASSWORD = 'passwordhere'


class CeleryConfig(object):
    from celery.schedules import crontab

    BROKER_URL = 'redis://localhost:6379'
    CELERY_BROKER = 'redis://localhost:6379'
    CELERY_BACKEND = 'redis://localhost:6379'

    CELERYBEAT_SCHEDULE = {
        'get_location_every_half_hour': {
            'task': 'tasks.save_current_location',
            'schedule': crontab(minute='*/30'),
        },
    }


class DevelopmentConfig(Config):
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
    LOGGER_HANDLER_POLICY = 'never'
