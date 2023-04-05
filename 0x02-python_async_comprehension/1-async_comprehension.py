#!/usr/bin/env python3
"""_summary_
    Yields:
        _type_: _description_
        should measure the total runtime and return it.
    """


import asyncio
import random
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Returns floatings numbers"""
    results = [i async for i in async_generator()]
    return results
