#!/usr/bin/env python3
"""
    3-tasks.py
    Write a function (do not create an async function,
    use the regular function syntax to do this) task_wait_random
    that takes an integer max_delay and returns a asyncio.Task.
"""

import asyncio
from typing import Task


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task[float]:
    """
        Returns:
        asyncio.Task[float]: An asyncio.Task object
        representing the execution of wait_random.
    """
    loop = asyncio.get_event_loop()
    return loop.create_task(wait_random(max_delay))
