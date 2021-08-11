import os

def persist_file(file_path, content_bytes):
    with open(file_path, 'wb') as stream:
        stream.write(content_bytes)

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)