import os, boto3
from dynaconf import settings


client = boto3.client('s3')


def upload(file_path, bucket, object_name):
    client.upload_file(file_path, bucket, object_name)