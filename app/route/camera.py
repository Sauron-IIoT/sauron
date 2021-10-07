from flask import Blueprint

import logging
from app.repository.capture import fetch_one_from_iot_device, persist_local, update_local
from app.service.classification import classify

capture_blueprint = Blueprint('capture', __name__)

@capture_blueprint.route('/capture', methods=['POST'])
def capture():
    capture = fetch_one_from_iot_device()
    capture['status'] = 'new'
    capture = persist_local(capture)

    capture = classify(capture)
    capture['status'] = 'classified'
    update_local(capture)

    logging.info(f'persisted capture to {capture["path"]}', extra=capture)

    return {"ACK"}