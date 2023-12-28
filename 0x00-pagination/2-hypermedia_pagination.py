#!/usr/bin/env python3
import csv
import math
from typing import List, Dict, Union


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
        '''return approproate page of dataset from index_range'''
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        idx, end_idx = index_range(page, page_size)
        return self.dataset()[idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10)\
            -> Dict[str, Union[int, List[list], None]]:
        '''this method returns a dictionary of key-value pairs'''
        page_data = self.get_page(page=page, page_size=page_size)
        total_pages = math.ceil(len(self.dataset()) / page_size)
        if 1 <= page <= total_pages:
            next_page = page + 1 if page < total_pages else None
            prev_page = page - 1 if page > 1 else None
            return {
                    'page_size': len(page_data),
                    'page': page,
                    'data': page_data,
                    'next_page': next_page,
                    'prev_page': prev_page,
                    'total_pages': total_pages
                    }
        else:
            return {
                    'page_size': 0,
                    'page': 0,
                    'data': [],
                    'next_page': None,
                    'prev_page': None,
                    'total_pages': total_pages
                    }


def index_range(page: int, page_size: int) -> tuple:
    '''this function returns a tuple containing a start index
    and an end index corresponding to the range of indexes to return
    in a list for those particular pagination parameters'''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
