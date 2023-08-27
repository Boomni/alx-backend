#!/usr/bin/env python3
"""LFU Cache"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """Caching System with LFU Algorithm"""

    def __init__(self):
        """Initialize"""
        super().__init__()
        self.frequency = {}  # To keep track of access frequency
        self.access_order = []  # To keep track of access order

    def put(self, key, item):
        """
        Assigns the item value to the dictionary
        self.cache_data for the key key
        """
        if key is None or item is None:
            return
        # Increment the access frequency or initialize it to 1
        self.frequency[key] = self.frequency.get(key, 0) + 1

        # Update access order
        self.access_order.append(key)

        # Check if cache is full
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            lfu_keys = [
                    key for key,
                    freq in self.frequency.items() if freq == min(self.frequency.values())
                    ]

            # If multiple items have the same least frequency,
            # use access order for tie-breaking
            if len(lfu_keys) > 1:
                lru_key = self.access_order.pop(0)
                if lru_key in lfu_keys:
                    lfu_keys.remove(lru_key)
                    del self.cache_data[lru_key]
                    del self.frequency[lru_key]
                    print(f"DISCARD: {lru_key}")

            # Evict the least frequency used item
            lfu_key = lfu_keys[0]
            del self.cache_data[lfu_key]
            del self.frequency[lfu_key]
            print(f"DISCARD: {lfu_key}")

        # Add the new item to the cache
        self.cache_data[key] = item

    def get(self, key):
        """Retrieve the item value linked to the key"""
        if key is None or key not in self.cache_data:
            return None
        # Increment the access frequency and update access order
        self.frequency[key] += 1
        self.access_order.remove(key)
        self.access_order.append(key)

        return self.cache_data[key]
