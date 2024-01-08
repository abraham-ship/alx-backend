#!/usr/bin/env python3
'''FIFO caching'''
from base_cacing import BaseCaching


class FIFOCache(BaseCaching):
    '''FIFO caching'''
    def __init__(self):
        '''initialization'''
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            discarded_key = next(iter(self.cache_data))
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}")

        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache[key]
