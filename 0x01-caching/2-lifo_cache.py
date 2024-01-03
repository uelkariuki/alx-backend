#!/usr/bin/env python3

"""
LIFO caching
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Class LIFOCache that inherits from BaseCaching
    """
    def __init__(self):
        """ Initialize"""
        super().__init__()

    def put(self, key, item):
        """ Implement the put method"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            del self.cache_data[key]

        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_key = next(reversed(list(self.cache_data.keys())))
            last_value = self.cache_data.pop(last_key)
            print(f'DISCARD: {last_key}')
        self.cache_data[key] = item

    def get(self, key):
        """ Implements the get method"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
