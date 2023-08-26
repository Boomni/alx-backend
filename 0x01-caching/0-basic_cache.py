#!/usr/bin/env python3
"""Basic Dictionary"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """Caching System"""

    def put(self, key, item):
        """Assigns to the disctionary the item value"""

        if item is None or key is None:
            pass
        else:
            self.cache_data[key] = item

    def get(self, key):
        if key is None or key not in self.cache_data.keys():
            return None
        return self.cache_data[key]
