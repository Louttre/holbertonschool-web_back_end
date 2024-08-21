#!/usr/bin/env python3
""" module """
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client.mydatabase
mongo_collection = db.school


def schools_by_topic(mongo_collection, topic):
    """
    Finds and returns all schools that include the specified topic.
    """
    collec = list(mongo_collection.find({ "topics": topic }))
    return collec