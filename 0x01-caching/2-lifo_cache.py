#!/usr/bin/env python3
"""LIFO Caching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Caching System with LIFO Algorithm"""

    def __init__(self):
        """Initialize"""
        super().__init__()

    def put(self, key, item):
        """
        Assigns to the dictionary self.cache_data
        the item value for the key key
        """
        if key is None or item is None:
            return

        # Check if cache is full
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Get the last (newest) key in the cache
            newest_key = self.cache_data[:-1]
            print(f"DISCARD: {newest_key}\n")
            del self.cache_data[newest_key]

        self.cache_data[key] = item

    def get(self, key):
        """Retrieves the item value by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
