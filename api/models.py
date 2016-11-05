import json

from .db.database import get_db
from . import app


class Location(object):

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

    def _build_compliment(compliment):
        return {'id': compliment['id'], 'text': compliment['text']} if compliment else abort(404)

    @classmethod
    def get_all(cls, json_repr=True):
        db = get_db()
        cur = db.execute('SELECT * FROM locations ORDER BY id DESC')
        rows = cur.fetchall()
        if json_repr:
            return json.dumps([dict(row) for row in rows])
        return rows

    @classmethod
    def get_latest(cls, json_repr=True):
        db = get_db()
        cur = db.execute('SELECT * FROM locations ORDER BY id DESC LIMIT 1')
        row = cur.fetchone()
        if json_repr:
            return json.dumps(dict(row))
        return row

    def save(self, json_repr=True):
        db = get_db()
        cur = db.execute("INSERT INTO locations (latitude, longitude) VALUES (?, ?)", (self.latitude, self.longitude))
        db.commit()
        return "Saved!"