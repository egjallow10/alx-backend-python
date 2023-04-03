#!/usr/bin/env python3
"""_summary_
return the list of all the delays (float values)
"""


import asyncio
from typing import List
from random import uniform
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: float) -> List[float]:
    """
    It returns the list of all the delays
    """
    tasks = []
    delays = []

    for i in range(n):
        task = wait_random(max_delay)
        tasks.append(task)

    for task in asyncio.as_completed((tasks)):
        delay = await task
        delays.append(delay)

    return delay
