#!/usr/bin/env python3
"""
    Module 12-log_stats.py
    Script that provides some stats
"""
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://:127.0.0.1:27017/")
db = client["logs"]
collection = db["nginx"]

# Get the total number of logs
total_logs = collection.count_documents({})

# Get the counts for each HTTP method
http_methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {method: collection.count_documents({"method": method}) for method in http_methods}

# Get the count for method=GET and path=/status
get_status_count = collection.count_documents({"method": "GET", "path": "/status"})

# Display the results
print(f"{total_logs} logs")
print("Methods:")
for method, count in method_counts.items():
    print(f"\t{method}: {count}")
print(f"GET requests with path=/status: {get_status_count}")
