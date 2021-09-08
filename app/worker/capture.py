import logging
from app.repository.capture import fetch_one_from_iot_device, persist_local, update_local
from app.service.classification import classify


def run():
    capture = fetch_one_from_iot_device()
    capture = persist_local(capture)
    capture = classify(capture)
    update_local(capture)
    logging.info(f'persisted capture to {capture["path"]}', extra=capture)