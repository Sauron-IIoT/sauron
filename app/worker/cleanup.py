import logging
from app.repository.capture import delete_all_uploaded

def run():
    capture_count = delete_all_uploaded()

    if (capture_count > 0):
        logging.info(f'deleted {capture_count} already uploaded capture(s) from local storage')
    else:
        logging.info(f'found nothing to cleanup')