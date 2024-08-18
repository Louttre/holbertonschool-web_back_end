#!/usr/bin/env python3
"""module"""


def floor(n: float) -> int:
    """
    Returns the largest integer less than or equal to the given floating-point number.
    
    This function converts the given float to an integer by truncating the decimal part,
    effectively rounding down towards zero.

    Parameters:
    n (float): The floating-point number to be floored.

    Returns:
    int: The largest integer less than or equal to the input number.
    """
    return int(n)
