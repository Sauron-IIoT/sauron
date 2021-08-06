import psycopg2
import psycopg2.extras

conn = psycopg2.connect("host=localhost dbname=temp user=admin password=sauron")
cursor = conn.cursor()

psycopg2.extras.register_uuid()


def persist_file(file_name, content_bytes):
    with open(file_name, 'wb') as stream:
        stream.write(content_bytes)

def query_capture_by_id(capture_id):
    return _query_one(f"select * from capture where id = '{capture_id}'")

def insert_capture(capture):
    cursor.execute(f"insert into capture (id, path, captured_at) values (%s, %s, %s)", 
        (capture['id'], capture['path'], capture['captured_at']))
    conn.commit()

def delete_capture_by_id(capture_id):
    cursor.execute(f"delete from capture where id = %s", capture_id)
    conn.commit()

def _query_all(query):
    cursor.execute(query)
    return cursor.fetchall()

def _query_one(query):
    cursor.execute(query)
    return cursor.fetchone()