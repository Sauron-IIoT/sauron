import logging
from app.repository.capture import fetch_all, persist_remote, delete_local

def run():
    captures = fetch_all()

    for capture in captures:
        persist_remote(capture)
        logging.info('capture uploaded to s3', extra=capture)

        delete_local(capture)
        logging.info('capture deleted from local storage', extra=capture)
