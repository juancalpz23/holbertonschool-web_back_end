#!/usr/bin/env python3
"""
    Module 11-schools_by_topic.py
"""
import pymongo


def schools_by_topic(mongo_collection, topic:str):
    """
        Search the school based in school
        and return a list
    """
    query: dict = {"topics": topic}
    schools: list = []

    for school in mongo_collection.fins(query):
        schools.append(school)

    return schools
