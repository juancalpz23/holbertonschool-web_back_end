#!/usr/bin/env python3
"""
    0-async_generator.py module
    Write a coroutine called async_generator that
    takes no arguments
"""

import asyncio
import random


async def async_generator():
    """
        Generate numbers and return float time random
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.randint(0, 10)
