#!/usr/bin/env python3
""" module """
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client.mydatabase
mongo_collection = db.school


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a document into the MongoDB collection and returns the inserted document's ID.
    """
    document = kwargs
    inserted_doc = mongo_collection.insert_one(document)
    inserted_doc_id = inserted_doc.inserted_id
    return inserted_doc_id
