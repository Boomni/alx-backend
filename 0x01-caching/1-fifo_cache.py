#!/usr/bin/env python3
"""FIFO Caching"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """Caching System with FIFO Algorithm"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.order = []  # To keep track of insertion order

    def put(self, key, item):
        """Assigns the item value to the dictionary self.cache_data for the key key"""
        if key is None or item is None:
            return

        # Check if cache is full
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Get the key to be removed (oldest)
            oldest_key = self.order[0]
            self.order = self.order[1:]  # Remove the oldest key
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")
        # Add the new item and update insertion order
        self.cache_data[key] = item
        self.order.append(key)

    def get(self, key):
        """Retrieves the item value by key"""
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
