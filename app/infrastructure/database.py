import psycopg2
from psycopg2.extras import register_uuid, RealDictCursor

conn = psycopg2.connect("host=database dbname=temp user=admin password=sauron")
cursor = conn.cursor(cursor_factory=RealDictCursor)

register_uuid()


def query_capture_by_id(capture_id):
    return _query_one(f"select * from capture where id = '{capture_id}'")

def insert_capture(capture):
    cursor.execute(f"insert into capture (id, path, captured_at, classification_score) values (%s, %s, %s, %s)", 
        (capture['id'], capture.get('path'), capture.get('captured_at'), capture.get('classification_score')))
    conn.commit()

def update_capture(capture):
    cursor.execute(f"update capture set path = %s, captured_at = %s, classification_score = %s where id = %s", 
        (capture.get('path'), capture.get('captured_at'), capture.get('classification_score'), capture['id']))
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