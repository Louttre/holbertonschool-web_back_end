#!/usr/bin/env python3
"""module"""
import asyncio
async_generator = __import__('0-async_generator').async_generator


async def print_yielded_values():
    """
    Asynchronous function that collects values yielded by async_generator
    into a list and then prints that list.
    """
    result = [i async for i in async_generator()]
    return result
