#!/usr/bin/env python3
"""Module to update school topics"""


def update_topics(mongo_collection, name, topics):
    """Change all topics of school document based on name"""
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
