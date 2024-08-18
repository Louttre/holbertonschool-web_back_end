#!/usr/bin/env python3
"""module"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Sums all the numbers in a list containing
    both integers and floating-point numbers,
    and returns the total as a float.

    Parameters:
    mxd_lst (list[float | int]): A list of
    numbers, which can include both 
    integers and floating-point values.

    Returns:
    float: The sum of all numbers in the
    input list, returned as a float.
    """
    i = 0
    for num in mxd_lst:
        i += num
    return i
