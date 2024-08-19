#!/usr/bin/env python3
"""module"""
import asyncio
import time
from random import uniform

async def async_generator():
    """
    An asynchronous generator that yields a random number between 0 and 10.

    The generator runs a loop 10 times. In each iteration, it waits asynchronously for 1 second 
    using asyncio.sleep(1), and then yields a random floating-point number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchronously wait for 1 second
        yield random.uniform(0, 10) 
