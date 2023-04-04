#!/usr/bin/env python3
"""_summary_
return a delay float values)
"""


import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    A task that waits for a random delay
    """
    return asyncio.create_task(wait_random(max_delay))
