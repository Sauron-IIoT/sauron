import psycopg2
from psycopg2.extras import register_uuid, RealDictCursor

conn = psycopg2.connect("host=database dbname=temp user=admin password=sauron")
cursor = conn.cursor(cursor_factory=RealDictCursor)

register_uuid()


def query_capture_by_id(capture_id):
    return _query_one(f"select * from capture where id = '{capture_id}'")

def query_uploaded_captures():
    return _query_many("select * from capture where is_uploaded = true")

def query_unuploaded_captures():
    return _query_many("select * from capture where is_uploaded = false")

def insert_capture(capture):
    cursor.execute(f"insert into capture (id, path, captured_at, classification_score) values (%s, %s, %s, %s)", 
        (capture['id'], capture.get('path'), capture.get('captured_at'), capture.get('classification_score')))
    conn.commit()

def update_capture(capture):
    cursor.execute(f"update capture set path = %s, captured_at = %s, classification_score = %s, is_uploaded = %s where id = %s", 
        (capture.get('path'), capture.get('captured_at'), capture.get('classification_score'), capture.get('is_uploaded'), capture['id']))
    conn.commit()

def delete_capture_by_id(capture_id):
    cursor.execute(f"delete from capture where id = %s", (capture_id,))
    conn.commit()

def _query_many(query):
    composed_query = f"select to_json(result) from ({query}) result;"
    cursor.execute(composed_query)
    result = cursor.fetchall()
    return [_as_json(row) for row in result]

def _query_one(query):
    composed_query = f"select to_json(result) from ({query}) result;"
    cursor.execute(composed_query)
    result = cursor.fetchone()
    return _as_json(result)

def _as_json(row):
    return row['to_json']