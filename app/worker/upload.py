import logging
from app.repository.capture import fetch_all_unuploaded, update_local, upload_to_s3
from app.repository.helix import create_capture as send_to_helix

def run():
    captures = fetch_all_unuploaded()

    for capture in captures:
        upload_to_s3(capture)
        send_to_helix(capture)

        capture['is_uploaded'] = True
        update_local(capture)

    if len(captures) > 0:
        logging.info(f'uploaded {len(captures)} capture(s) to S3 and Helix')
    else:
        logging.info(f'found nothing to upload')