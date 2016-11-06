from flask import Flask, jsonify
from pyicloud import PyiCloudService
import logging
from logging.handlers import RotatingFileHandler
import werkzeug

from .celery_helper import make_celery
from celery.schedules import crontab

app = Flask(__name__, instance_relative_config=True)

app.config.from_object('config.DevelopmentConfig')
app.config.from_pyfile('config.py', silent=True)

celery = make_celery(app)
icloud = PyiCloudService(app.config['ICLOUD_USER'], app.config['ICLOUD_PASSWORD'])

handler = RotatingFileHandler('error.log', maxBytes=10000, backupCount=1)
handler.setLevel(logging.INFO)
handler.setFormatter(logging.Formatter(
    '%(asctime)s %(levelname)s: %(message)s '
    '[in %(pathname)s:%(lineno)d]'
))

app.logger.addHandler(handler)


@app.errorhandler(werkzeug.exceptions.NotFound)
def handle_bad_request(e):
    return jsonify({'message': 'Oops, nothing to see here.'})


from .db.database import initdb_command

from .tasks import *
from .views import *