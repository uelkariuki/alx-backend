#!/usr/bin/env python3

"""
LRU caching
"""

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """
    Class LRUCache that inherits from BaseCaching
    """
    def __init__(self):
        """ Initialize"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Implement the put method"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            del self.cache_data[key]
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            last_value = self.cache_data.popitem(last=False)
            print(f'DISCARD: {last_value[0]}')
        self.cache_data[key] = item
        self.cache_data.move_to_end(key)

    def get(self, key):
        """ Implements the get method"""
        if key is None or key not in self.cache_data:
            return None

        value = self.cache_data.pop(key)
        # move the key to the end
        self.cache_data[key] = value
        return value
