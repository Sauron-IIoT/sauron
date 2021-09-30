import requests
import json
from dynaconf import settings


headers_post = {
    'Content-Type': 'application/json',
    'fiware-service': 'helixiot',
    'fiware-servicepath': '/'
}


def create_capture(capture):

    entity_type = capture['prediction_label']

    if entity_type == None:
        entity_type = 'prediction_failure'

    helix_capture = {
        'uuid': capture['id'],
        'captured_at': capture['captured_at'],
        'prediction_label': entity_type,
        'prediction_confidence': capture['prediction_confidence']
    }
    helix_capture['id'] = f'urn:ngsi-ld:capture:{capture["id"]}'
    helix_capture['type'] = entity_type

    response = requests.post(f'{settings["broker_address"]}/v2/entities?options=keyValues',
                             data=json.dumps(helix_capture), headers=headers_post)
    response.raise_for_status()