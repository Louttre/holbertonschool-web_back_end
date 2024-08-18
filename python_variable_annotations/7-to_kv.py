#!/usr/bin/env python3
"""module"""


def to_kv(k: str, v: int | float) -> tuple[str, float]:
    """    
    Creates a tuple with a string and the square of a number.

    Parameters:
    k (str): The key, represented as a string.
    v (int | float): A number that can be either an integer or a float.

    Returns:
    tuple[str, float]: A tuple where the first element is the string `k`, 
    and the second element is the square of `v`, represented as a float.
    """
    return (k, v * v)
