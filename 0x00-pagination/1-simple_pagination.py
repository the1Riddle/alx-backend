import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
        """
            my method
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
        """
            Get the requested page
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page > 0 and page_size > 0 
        page, page_size = index_range(page, page_size)

        if page >= len(self.dataset()):
            return []
        page_size = min(page_size, len(self.dataset()))
        return self.dataset()[page:page_size]
        pass
