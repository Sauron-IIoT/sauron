import psycopg2
from psycopg2.extras import register_uuid, RealDictCursor

conn = psycopg2.connect("host=database dbname=temp user=admin password=sauron")
conn.autocommit = True
cursor = conn.cursor(cursor_factory=RealDictCursor)

register_uuid()


def query_capture_by_id(capture_id):
    return _query_one(f"select * from capture where id = '{capture_id}'")

def query_uploaded_captures():
    return _query_many("select * from capture where status = 'uploaded'")

def query_classified_captures():
    return _query_many("select * from capture where status = 'classified'")

def insert_capture(capture):
    cursor.execute(f"insert into capture (id, path, captured_at, prediction_label, prediction_confidence, status) values (%s, %s, %s, %s, %s, %s)", 
        (capture['id'], capture.get('path'), capture.get('captured_at'), capture.get('prediction_label'), capture.get('prediction_confidence'), capture.get('status')))

def update_capture(capture):
    cursor.execute(f"update capture set path = %s, captured_at = %s, prediction_label = %s, prediction_confidence = %s, status = %s where id = %s", 
        (capture.get('path'), capture.get('captured_at'), capture.get('prediction_label'), capture.get('prediction_confidence'), capture.get('status'), capture['id']))

def delete_capture_by_id(capture_id):
    cursor.execute(f"delete from capture where id = %s", (capture_id,))

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