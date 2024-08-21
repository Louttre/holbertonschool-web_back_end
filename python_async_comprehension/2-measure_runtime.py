#!/usr/bin/env python3
"""module"""
import asyncio
import time
from typing import float

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    This coroutine measures the total time
    taken to execute
    four instances of the async_comprehension
    coroutine in parallel.
    """
    start = time.perf_counter()
    await asyncio.gather(async_comprehension(), async_comprehension(),
                        async_comprehension(), async_comprehension())
    end = time.perf_counter()
    return end - start
