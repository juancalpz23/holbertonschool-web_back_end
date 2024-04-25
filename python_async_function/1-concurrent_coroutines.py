#!/usr/bin/env python3
"""
    1-concurrent_coroutines.py module
    Async routine that spawns wait_random n
    times with the specified max_delay.
"""

import asyncio
import random
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
        Returns:
        List[float]: List of all the delays
        (float values) in ascending order.
    """

    delays: List[float] = []
    tasks: List = []

    for _ in range(n):
        tasks.append(wait_random(max_delay))
    
    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)

    return delays

