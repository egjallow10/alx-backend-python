#!/usr/bin/env python3
"""Function should return a float.
and iport from other files
"""


import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Returns time"""
    init_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_time = time.time()
    total_time = end_time - init_time
    return (total_time/n)
