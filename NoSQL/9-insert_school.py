#!/usr/bin/env python3
"""
    Module 9-insert_school
"""
import pymongo


def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document in a collection based on kwargs
    """
    new_school = mongo_collection.insert_one(kwargs)

    return (new_school.inserted_id)
