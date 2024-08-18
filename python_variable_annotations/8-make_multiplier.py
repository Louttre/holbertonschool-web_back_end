#!/usr/bin/env python3
"""module"""
from typing import Callable


def make_multiplier(v: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies its input by a specified value.

    Parameters:
    v (float): The value by which the returned function will multiply its input.

    Returns:
    Callable[[float], float]: A function that takes a float as input and returns 
    the product of that input and `v`.
    """
    def multiplier(a: float) -> float:
        return a * v
    return multiplier
