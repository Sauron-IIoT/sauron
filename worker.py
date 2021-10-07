import os, time, logging
import app.worker.capture as capture
import app.worker.upload as upload
import app.worker.cleanup as cleanup
from app.config.logging import config as config_logger

config_logger()
worker_name = os.getenv('SAURON_WORKER_NAME')
worker_sleep = int(os.getenv('SAURON_WORKER_SLEEP'))

while(True):
    try:
        if worker_name == 'capture':
            capture.run()
        elif worker_name == 'upload':
            upload.run()
        elif worker_name == 'cleanup':
            cleanup.run()
        else:
            raise ValueError(f'unknown worker: {worker_name}')
    except Exception as ex:
        logging.error(f'Unexpected error running {worker_name}: {ex}')

    logging.info(f'sleeping for {worker_sleep} seconds...')

    time.sleep(worker_sleep)
