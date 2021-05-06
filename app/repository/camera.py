import requests
import uuid
from dynaconf import settings


def capture():
    capture_bytes = requests.get(settings['camera_address']).content
    capture_id = uuid.uuid4()

    with open(f'captures/{capture_id}.jpg', 'wb') as stream:
        stream.write(capture_bytes)

    return capture_id
