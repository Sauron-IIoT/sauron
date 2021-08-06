import requests
from dynaconf import settings


camera_address = settings['camera_address']


def capture():
    return requests.get(camera_address).content
