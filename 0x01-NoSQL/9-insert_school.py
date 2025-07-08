#!/usr/bin/env python3
"""This is a module that inserts a doc using pymongo
"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a doc"""
    doc = {**kwargs}
    result = mongo_collection.insert_one(doc)
    id = result.inserted_id
    return id
