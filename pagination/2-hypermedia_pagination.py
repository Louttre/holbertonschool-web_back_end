from typing import Tuple
import csv
import math
from typing import List
"""module"""


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end indices
    for a given page and page size in pagination.
    """
    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert isinstance(page, int) and page > 0, "Page should be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, "Page_size should be a positive integer"
        dataset = self.dataset()
        start_index, end_index = index_range(page, page_size)
        if start_index >= len(dataset):
            return []
        return dataset[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Optional[int]]:
        dataset = self.get_page(page, page_size)
        start_index, end_index = index_range(page, page_size)
        next_page = page + 1 if end_index < len(dataset) else None
        prev_page = page - 1 if page > 1 else None
        total_pages = math.ceil(len(dataset) / page_size)
        return {
              'page_size': page_size,
              'page': page,
              'data': dataset,
              'next_page': next_page,
              'prev_page': prev_page,
              'total_pages': total_pages
         }
              
