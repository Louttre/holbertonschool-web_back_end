#!/usr/bin/env python3
"""module"""
import asyncio
from typing import List


async_generator = __import__('0-async_generator').async_generator


async def print_yielded_values() -> List[float]:
    """
    Asynchronous function that collects values yielded by async_generator
    into a list and then prints that list.
    """
    return result = [i async for i in async_generator()]
