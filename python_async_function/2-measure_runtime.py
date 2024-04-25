#!/usr/bin/env python3
"""
    2-measure_runtime.py module
    Create a measure_time function with integers n
    and max_delay as arguments that measures the total
    execution time for wait_n(n, max_delay), and returns
    total_time / n. Your function should return a float.
    Use the time module to measure an approximate elapsed time.
"""

import time
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int = 0, max_delay: int = 10) -> float:
    """
        Measure the average execution time for
        wait_n(n, max_delay)
    """
    start_time = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed = time.perf_counter() - start_time
    total_time = elapsed / n

    return total_time
