#!/usr/bin/env python3
"""
    4-tasks.py module
    Take the code from wait_n and alter it into a
    new function task_wait_n. The code is nearly
    identical to wait_n except task_wait_random is
    being called.
"""

import asyncio
from typing import List


task_wait_random = __import__('3-tasks').wait_random


async def task_wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
        Returns multiples tasks
    """
    delays: List[float] = []
    tasks: List[asyncio.Task] = []

    for _ in range(n):
        tasks.append(task_wait_random(max_delay))

    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)

    return delays
