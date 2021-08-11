import os, uuid, datetime
from dynaconf import settings
from app.infrastructure.filesystem import persist_file, delete_file
from app.infrastructure.database import insert_capture, update_capture, query_capture_by_id, query_all_captures, delete_capture_by_id
from app.infrastructure.s3 import upload
from app.infrastructure.iot_camera import capture


s3_bucket = settings['s3_bucket']


def fetch_one_from_iot_device():
    new_id = uuid.uuid4()
    return {
        'id': new_id,
        'content_bytes': capture(),
        'captured_at': datetime.datetime.now().isoformat()
    }

def fetch_by_id(capture_id):
    return query_capture_by_id(capture_id)

def fetch_all():
    return query_all_captures()

def persist_local(capture):
    capture['path'] = f'./captures/{capture["id"]}.jpg'
    persist_file(capture['path'], capture['content_bytes'])
    insert_capture(capture)
    return fetch_by_id(capture['id'])

def update_local(capture):
    update_capture(capture)
    return fetch_by_id(capture['id'])

def persist_remote(capture):
    upload(capture['path'], s3_bucket, f'{capture["id"]}.jpg')

def delete_local(capture):
    delete_capture_by_id(capture["id"])
    delete_file(capture["path"])