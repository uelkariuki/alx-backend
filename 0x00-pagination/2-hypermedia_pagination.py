#!/usr/bin/env python3

"""Hypermedia Pagination """
import csv
import importlib
import math
from typing import Dict, List

Index_range = importlib.import_module('0-simple_helper_function')


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
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0
        try:
            dataset = self.dataset()
        except FileNotFoundError:
            return []
        start_idx, end_idx = Index_range.index_range(page, page_size)
        return dataset[start_idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Returns a dictionary containing key-value pairs to showcase hypermedia
        pagination
        """
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)
        page = page
        data = self.get_page(page, page_size)
        page_size = len(data)

        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
            }
