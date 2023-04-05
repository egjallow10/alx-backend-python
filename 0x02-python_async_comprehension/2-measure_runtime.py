#!/usr/bin/env python3
"""_summary_
    Yields:
        _type_: _description_
        should measure the total runtime and return it.
    """


import asyncio
from typing import List
async_comprehension = __import__('1-async_comprehension').async_comprehension
import time


async def measure_runtime() -> float:
    start_time = asyncio.get_running_loop().time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = asyncio.get_running_loop().time()
    return end_time - start_time
