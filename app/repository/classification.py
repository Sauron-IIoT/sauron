import json, requests
from dynaconf import settings

classification_address = settings['classification_address']


def classify(image_path):
    payload = {
        "image": image_path
    }
    response = requests.post(f'{classification_address}/classification', data=json.dumps(payload))
    response.raise_for_status()

    return json.loads(response.text)