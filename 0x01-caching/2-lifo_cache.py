#!/usr/bin/env python3
"""LIFO Caching"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """Caching System with LIFO Algorithm"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Assigns the item value to the dictionary self.cache_data for the key key"""
        if key is None or item is None:
            return

        # Check if cache is full
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Get the key to be removed (latest)
            latest_key = self.order.pop()
            del self.cache_data[latest_key]
            print(f"DISCARD: {latest_key}")

        # Add the new item and update insertion order
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Retrieves the item value by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
