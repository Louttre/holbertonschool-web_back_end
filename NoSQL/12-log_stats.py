#!/usr/bin/env python3
#!/usr/bin/env python3
""" Write a Python script that provides some stats about
    Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


if __name__ == "__main__":
    """ Database: logs
        Collection: nginx
    """

    client = MongoClient("mongodb://localhost:27017/")
    db = client.logs
    mongo_collection = db.nginx
    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print(f'{mongo_collection.count_documents()} logs')
    print("Methods:")
    for met in method:
        count = mongo_collection.count_documents({ "method": met })
        print(f'\tmethod {met}: {count}')
    status_check_count = mongo_collection.count_documents(
        { "method": "GET", "path": "/status" }
    )
    print(f'{status_check_count} status check')
