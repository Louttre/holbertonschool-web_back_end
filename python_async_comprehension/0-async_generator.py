#!/usr/bin/env python3
"""module"""
import asyncio
import random
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    """
    An asynchronous generator that yields a random number between 0 and 10.

    The generator runs a loop 10 times. In each iteration, it waits asynchronously for 1 second 
    using asyncio.sleep(1), and then yields a random floating-point number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10) 
