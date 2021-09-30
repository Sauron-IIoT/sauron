import logging
from app.repository.capture import fetch_all_classified, update_local, upload_to_s3
from app.repository.helix import create_capture as send_to_helix

def run():
    captures = fetch_all_classified()

    for capture in captures:
        upload_to_s3(capture)
        send_to_helix(capture)

        capture['status'] = 'uploaded'
        update_local(capture)

    if len(captures) > 0:
        logging.info(f'uploaded {len(captures)} capture(s) to S3 and Helix')
    else:
        logging.info(f'found nothing to upload')