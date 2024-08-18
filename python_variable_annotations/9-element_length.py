#!/usr/bin/env python3
"""module"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Creates a list of tuples where each tuple contains an element from the input iterable
    and its length.

    Parameters:
    lst (Iterable[Sequence]): An iterable containing sequences (such as lists, strings, 
    or tuples). Each element in `lst` should be a sequence.

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples where each tuple consists of a sequence 
    from the input
    """
    return [(i, len(i)) for i in lst]
