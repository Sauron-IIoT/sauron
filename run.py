import os, time, sys
import app.worker.capture_and_save_local as capture_and_save_worker
import app.worker.upload_to_s3_and_delete_local as upload_to_s3_worker
from app.config.logging import config as config_logger

config_logger()
worker_name = os.getenv('SAURON_WORKER_NAME')

while(True):
    if worker_name == 'capture_and_save':
        capture_and_save_worker.run()
    elif worker_name == 'upload_to_s3':
        upload_to_s3_worker.run()
    else:
        raise ValueError(f'unknown worker: {worker_name}')

    time.sleep(10)
