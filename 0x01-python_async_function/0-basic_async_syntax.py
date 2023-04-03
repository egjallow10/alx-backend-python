#!/usr/bin/env python3
"""The basic of async that perform asyanc
operarin
"""


import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Return a  float """
    delay = random.random() * max_delay
    await asyncio.sleep(delay)
    return delay
