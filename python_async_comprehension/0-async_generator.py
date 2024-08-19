#!/usr/bin/env python3
"""module"""
import asyncio
import time
from random import random


async def async_generator():
    """
    An asynchronous generator that produces random numbers.

    This generator yields 10 random floating-point numbers between 0 and 1, with a 1-second delay between each.
    It uses `await asyncio.sleep(1)` to pause execution for 1 second before generating and yielding the next number.

    Returns:
    - `float`: A random floating-point number between 0 and 1.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        ran = random()
        yield ran
