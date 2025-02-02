#!/usr/bin/env python3
"""Script that provides stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx = db.nginx

    # Get total logs count
    total_logs = nginx.count_documents({})
    print(f"{total_logs} logs")

    # Get methods stats
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        count = nginx.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Get status check count
    status_checks = nginx.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_checks} status check")
