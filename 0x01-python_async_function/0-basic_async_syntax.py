#!/usr/bin/env python3
"""The basic of async"""


import asyncio
import random


async def wait_random( max_delay: int = 10) -> float:
    """Return a a float """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
