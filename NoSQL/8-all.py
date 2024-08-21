#!/usr/bin/env python3
"""module"""
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client.mydatabase
mongo_collection = db.school


def list_all(mongo_collection):
    """
    Lists all documents in the provided MongoDB collection.
    """
    list_collec = list(mongo_collection.find())
    return list_collec if list_collec else []