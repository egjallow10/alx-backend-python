#!/usr/bin/env python3
"""_summary_

    Returns:
        _type_: _description_
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
        tasks.append(asyncio.create_task(wait_random(max_delay)))

    for delay in await asyncio.gather(*tasks):
        delays.append(delay)
    delays.sort()

    return delays
