import uuid
import datetime
from dynaconf import settings
from app.infrastructure.local_storage import persist_file, insert_capture, query_capture_by_id, \
                                             query_all_captures, delete_capture_by_id, delete_file
from app.infrastructure.s3 import upload
from app.infrastructure.camera import capture


s3_bucket = settings['s3_bucket']


def fetch_one():
    new_id = uuid.uuid4()
    return {
        'id': new_id,
        'content_bytes': capture(),
        'captured_at': datetime.datetime.now().isoformat()
    }

def get_by_id(capture_id):
    return query_capture_by_id(capture_id)

def get_all():
    return query_all_captures()

def save_local(capture):
    capture['path'] = f'captures/{capture["id"]}.jpg'
    persist_file(capture['path'], capture['content_bytes'])
    insert_capture(capture)

def save_remote(capture):
    upload(capture['path'], s3_bucket, f'{capture["id"]}.jpg')

def delete_local(capture):
    delete_capture_by_id(capture["id"])
    delete_file(capture["path"])