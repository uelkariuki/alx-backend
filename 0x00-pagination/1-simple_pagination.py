#!/usr/bin/env python3

"""
Simple pagination
"""
import csv
import math
from typing import Tuple, List


def index_range(page: int, page_size: int) -> Tuple:
    """
    Return a tuple of size two containing a start index and an end index
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return start_index, end_index


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
        Returns the appropriate page of the dataset (i.e. the correct list
        of rows)
        """
        assert page > 0
        assert type(page) == int
        assert type(page_size) == int
        assert page_size > 0
        try:
            dataset = self.dataset()
        except FileNotFoundError:
            return []
        start_idx, end_idx = index_range(page, page_size)
        end_idx = min(end_idx, len(dataset))

        if start_idx >= end_idx:
            return []
        return dataset[start_idx:end_idx]
