#!/usr/bin/env python3
"""Module to list documents in MongoDB collection"""


def list_all(mongo_collection):
    """List all documents in a collection"""
    if mongo_collection is None:
        return []
    return list(mongo_collection.find())
