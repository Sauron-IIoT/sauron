import logging
from app.repository.capture import fetch_one_from_iot_device, persist_local, update_local
from app.service.classification import classify


def run():
    capture = fetch_one_from_iot_device()
    logging.info('capture fetched from camera', extra=capture)

    persist_local(capture)
    logging.info('capture persisted to local storage', extra=capture)

    capture = classify(capture)
    logging.info(f'capture classification score is {capture["classification_score"]}', extra=capture)

    update_local(capture)
    logging.info('capture score updated', extra=capture)