from typing import Tuple
"""module"""


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indices
    for a given page and page size in pagination.
    """
    index = (page - 1) * page_size
    index_end = page * page_size
    return (index, index_end)
