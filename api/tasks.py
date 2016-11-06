from .models import Location
from . import celery, icloud


@celery.task(name='tasks.save_current_location')
def save_current_location():
    location = icloud.iphone.location()
    Location(latitude=location['latitude'], longitude=location['longitude']).save()
