#!/usr/bin/env python3
"""_summary_
return the list of all the delays (float values)
"""


import asyncio
from typing import List
from random import uniform
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Retunrs an array of await floats"""
    tasks = [wait_random(max_delay) for i in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
