import os
import psycopg2
from psycopg2.extras import register_uuid, RealDictCursor

conn = psycopg2.connect("host=localhost dbname=temp user=admin password=sauron")
cursor = conn.cursor(cursor_factory=RealDictCursor)

register_uuid()


def persist_file(file_path, content_bytes):
    with open(file_path, 'wb') as stream:
        stream.write(content_bytes)

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)

def query_capture_by_id(capture_id):
    return _query_one(f"select * from capture where id = '{capture_id}'")

def insert_capture(capture):
    cursor.execute(f"insert into capture (id, path, captured_at) values (%s, %s, %s)", 
        (capture['id'], capture['path'], capture['captured_at']))
    conn.commit()

def delete_capture_by_id(capture_id):
    cursor.execute(f"delete from capture where id = %s", (capture_id,))
    conn.commit()

def query_all_captures():
    return _query_all(f"select * from capture")

def _query_all(query):
    composed_query = f"select array_agg(t) from ({query}) t;"
    cursor.execute(query)
    return cursor.fetchall()

def _query_one(query):
    cursor.execute(query)
    return cursor.fetchone()