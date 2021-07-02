import psycopg2

db_conn = psycopg2.connect("dbname='postgres' user='postgres' password='sauron'")
db_cursor = db_conn.cursor()


def save_file(file_name, content_bytes):
    with open(file_name, 'wb') as stream:
        stream.write(content_bytes)

def get_capture_by_id(capture_id):
    return fetchone(f"select * from capture where id = '{capture_id}'")

def _query_all(query):
    cursor.execute(query)
    return cursor.fetchall()

def _query_one(query):
    cursor.execute(query)
    return cursor.fetchone()