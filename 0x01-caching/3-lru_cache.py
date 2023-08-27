#!/usr/bin/env python3
"""LRU Cache"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """Caching System with LRU Algorithm"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.order = []  # To keep track of access order

    def put(self, key, item):
        """
        Assigns the item value to the dictionary self.cache_data
        for the key key
        """
        if key is None or item is None:
            return

        # Check if cache is full
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Get the key to be removed (least recently used)
            lru_key = self.order.pop(0)
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}")

        # Add the new item and update access order
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Retrieve the item value linked to the key"""
        if key is None or key not in self.cache_data:
            return None

        # Move the accessed key to the end of the access order
        self.order.remove(key)
        self.order.append(key)

        return self.cache_data[key]
