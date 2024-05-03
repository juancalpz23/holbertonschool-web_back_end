#!/usr/bin/env python3
"""
    Module 12-log_stats.py
    Script that provides log stats
"""
from pymongo import MongoClient


if __name__ == "__main__":
    """
    Function that provides some stats about Nginx logs stored in MongoDB
    """
    client = MongoClient("mongodb://127.0.0.1:27017/")
    collection = client.logs.nginx

    print(f"{collection.estimated_document_count()} logs")
    print("Methods:")

    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    get = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{get} status check")
