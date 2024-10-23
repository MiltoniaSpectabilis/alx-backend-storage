#!/usr/bin/env python3
"""Module to insert document in MongoDB collection"""


def insert_school(mongo_collection, **kwargs):
    """Insert a document into a collection"""
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
