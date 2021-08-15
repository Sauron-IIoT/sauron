import uuid
import requests
import json
from dynaconf import settings


headers_post = {
    'Content-Type': 'application/json',
    'fiware-service': 'helixiot',
    'fiware-servicepath': '/'
}


def create_capture(capture):
    helix_capture = capture.copy()
    helix_capture['id'] = f'urn:ngsi-ld:capture:{capture["id"]}'
    helix_capture['type'] = 'capture'

    response = requests.post(f'{settings["broker_address"]}/v2/entities',
                             data=json.dumps(helix_capture), headers=headers_post)
    print(response.text)
    response.raise_for_status()