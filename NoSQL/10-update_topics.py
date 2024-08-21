#!/usr/bin/env python3
""" module """
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client.mydatabase
mongo_collection = db.school


def update_topics(mongo_collection, name, topics):
    """
    Updates the 'topics' field for all documents with the given 'name'.
    """
    mongo_collection.update_many({ "name": name }, {"$set":{ "topics": topics}})
