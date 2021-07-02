import requests
import uuid
import datetime
from dynaconf import settings
from app.infrastructure.local_storage import save_file

camera_address = settings['camera_address']

def capture():
    new_id = uuid.uuid4()
    return {
        'id': new_id
        'content_bytes': requests.get(camera_address).content
        'captured_at': datetime.datetime.now().isoformat()
        'path': f'captures/{new_id}.jpg'
    {

def save(capture):
    save_file(capture['path'], capture['content_bytes'])


