#!/usr/bin/env python3
"""
    Module 10-update_topics.py
"""
import pymongo
from typing import List


def update_topics(mongo_collection, name, topics):
    """
        Function that changes all topics of a school based on name
    """
    query: dict = {"name": name}
    mongo_collection.update_many(query, {"$set": {"topics": topics}})
