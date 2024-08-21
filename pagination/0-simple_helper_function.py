#!/usr/bin/env python3
"""module"""
from typing import Tuple



def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indices
    for a given page and page size in pagination.
    """
    return ((page - 1) * page_size, page * page_size)
