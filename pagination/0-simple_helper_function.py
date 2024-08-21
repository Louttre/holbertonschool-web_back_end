#!/usr/bin/env python3
from typing import Tuple
"""module"""


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indices
    for a given page and page size in pagination.
    """
    idx = page * page_size - page_size
    index = page * page_size
    return (idx, index)
