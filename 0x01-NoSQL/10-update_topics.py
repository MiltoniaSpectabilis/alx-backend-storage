#!/usr/bin/env python3
"""This module updates a doc using pymongo
"""


def update_topics(mongo_collection, name, topics):
    """Updates a doc"""
    mongo_collection.update_one(
        {'name': name},
        {"$set": {'topics': topics}},
        upsert=True
    )
