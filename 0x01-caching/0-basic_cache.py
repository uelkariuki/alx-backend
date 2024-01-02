#!/usr/bin/env python3
"""
Basic dictionary
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    Class BasicCache that inherits from BaseCaching
    """
    def put(self, key, item):
        """ Implements the put method"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Implements the get method"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data.get(key)
