#!/usr/bin/env python3

"""
LFU caching
"""

from base_caching import BaseCaching
from collections import Counter, OrderedDict


class LFUCache(BaseCaching):
    """
    Class LFUCache that inherits from BaseCaching
    """
    def __init__(self):
        """ Initialize"""
        super().__init__()
        self.cache_data = OrderedDict()
        self.frequency = Counter()

    def put(self, key, item):
        """ Implement the put method"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.cache_data.move_to_end(key)
            self.frequency[key] += 1
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                least_frequent_key, _ = min(self.frequency.items(),
                                            key=lambda x:
                                            (x[1],
                                             list(self.cache_data.keys()).
                                             index(x[0])))

                del self.cache_data[least_frequent_key]
                del self.frequency[least_frequent_key]
                print(f'DISCARD: {least_frequent_key}')

            self.cache_data[key] = item
            self.frequency[key] = 1

    def get(self, key):
        """ Implements the get method"""
        if key is None or key not in self.cache_data:
            return None

        self.cache_data.move_to_end(key)
        self.frequency[key] += 1
        # move the key to the end
        return self.cache_data[key]
