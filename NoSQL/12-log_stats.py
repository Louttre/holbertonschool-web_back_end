#!/usr/bin/env python3
""" module """
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client.logs
mongo_collection = db.nginx


method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
print(f'{mongo_collection.count_documents()} logs')
print("Methods :")
for met in method:
    print(f'\tmethod {met}: {mongo_collection.count_documents({ "method": met })}')
status_check_count = mongo_collection.count_documents({ "method": "GET", "path": "/status" })
print(f'{status_check_count} status check')
