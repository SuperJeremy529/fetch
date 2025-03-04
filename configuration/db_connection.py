from mongoengine import connect
from environments import *

def create_database_connection():
    uri = f"mongodb://{MONGO_DATABASE_USERNAME}:{MONGO_DATABASE_PASSWORD}@{MONGO_DATABASE_HOST}:{MONGO_DATABASE_PORT}"
    connect(host=uri)