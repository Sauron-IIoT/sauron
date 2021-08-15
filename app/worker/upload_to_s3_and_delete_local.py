import logging
from app.repository.capture import fetch_all, persist_remote as send_to_s3, delete_local
from app.repository.helix import create_capture as send_to_helix

def run():
    captures = fetch_all()

    for capture in captures:
        send_to_s3(capture)
        logging.info('capture uploaded to s3', extra=capture)

        send_to_helix(capture)
        logging.info('capture sent to helix', extra=capture)
        
        delete_local(capture)
        logging.info('capture deleted from local storage', extra=capture)
