#!/usr/bin/env python3
"""module"""
from typing import Callable



def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Creates a multiplier function that mu
    ltiplies its input by a specified value.

    Parameters:
    multiplier (float): The value by w
    ich the returned function will multiply its input.

    Returns:
    Callable[[float], float]: A function
    that takes a float as input and returns
    the product of that input and `multiplier`.
    """
    return lambda n: (n * multiplier)
