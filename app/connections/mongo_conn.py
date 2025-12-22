from pymongo import MongoClient
from constants import MONGO_STRING
def get_mongo_client():
    client = MongoClient(MONGO_STRING)
    return client

def get_db():
    client = get_mongo_client()
    return client["logs"]
