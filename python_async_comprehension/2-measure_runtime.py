#!/usr/bin/env python3
"""module"""
import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
    """
    This coroutine measures the total time
    taken to execute
    four instances of the async_comprehension
    coroutine in parallel.
    """
    start = time.time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )
    end = time.time()
    return end - start
