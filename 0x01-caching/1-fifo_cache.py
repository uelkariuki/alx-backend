#!/usr/bin/env python3

"""
FIFO caching
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    Class FIFOCache that inherits from BaseCaching
    """
    def __init__(self):
        """ Initialize"""
        super().__init__()

    def put(self, key, item):
        """ Implement the put method"""
        if key is None or item is None:
            return
        if (len(self.cache_data) >= BaseCaching.MAX_ITEMS and
                key not in self.cache_data):
            first_key = next(iter(self.cache_data))
            first_value = self.cache_data.pop(first_key)
            print(f'DISCARD: {first_key}')
        self.cache_data[key] = item

    def get(self, key):
        """ Implements the get method"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
