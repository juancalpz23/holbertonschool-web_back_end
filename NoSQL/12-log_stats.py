#!/usr/bin/env python3
"""
    Module 12-log_stats.py
    Script that provides log stats
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db_nginx = client.logs.nginx
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    count_logs = db_nginx.count_documents({})
    print(f'{count_logs} logs')

    print('Methods:')
    for method in methods:
        count_method = db_nginx.count_documents({'method': method})
        print(f'\tmethod {method}: {count_method}')

    check = db_nginx.count_documents(
        {"method": "GET", "path": "/status"}
    )

    print(f'{check} status check')
