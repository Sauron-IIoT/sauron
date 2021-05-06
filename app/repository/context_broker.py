import uuid
import requests
import json
from dynaconf import settings

headers_post = {
    'Content-Type': 'application/json',
    'fiware-service': 'helixiot',
    'fiware-servicepath': '/'
}

headers_get = {
    'Accept': 'application/json',
    'fiware-service': 'helixiot',
    'fiware-servicepath': '/'
}


def create_product(product):
    product_id = uuid.uuid4()
    product['id'] = f'urn:ngsi-ld:product:{product_id}'

    response = requests.post(f'{settings["broker_address"]}/v2/entities',
                             data=json.dumps(product), headers=headers_post)
    response.raise_for_status()

    return product_id


def get_product(product_id):
    return json.loads(requests.get(f'{settings["broker_address"]}/v2/entities/urn:ngsi-ld:product:{product_id}',
                                   headers=headers_get).text)
