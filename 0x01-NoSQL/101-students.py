#!/usr/bin/env python3
"""Module to calculate top students by average score"""


def top_students(mongo_collection):
    """Returns all students sorted by average score"""
    # Use aggregation pipeline to calculate average scores
    pipeline = [
        {
            "$project": {
                "name": 1,
                "topics": 1,
                "averageScore": {
                    "$avg": "$topics.score"
                }
            }
        },
        {
            "$sort": {
                "averageScore": -1
            }
        }
    ]

    return list(mongo_collection.aggregate(pipeline))
