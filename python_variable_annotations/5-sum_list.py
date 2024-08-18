#!/usr/bin/env python3
"""module"""


def sum_list(input_list: list[float]) -> float:
    """
    Sums all the floating-point numbers in a list and returns the total.

    Parameters:
    input_list (list[float]): A list of floating-point numbers to be summed.

    Returns:
    float: The sum of all numbers in the input list.
    """

    i = 0
    for num in input_list:
        i += num
    return i
