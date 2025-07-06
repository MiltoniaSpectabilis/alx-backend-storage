#!/usr/bin/env python3
"""This module lists all docs in a collection (MongoDB)
"""


def list_all(mongo_collection):
    """Returns all docs found in the collection"""
    all_docs = mongo_collection.find()
    return all_docs
