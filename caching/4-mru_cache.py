#!/usr/bin/python3


"""
    MRUCache module
"""


from base_caching import BaseCaching


class MRUCache(BaseCaching):

    """
        MRUCache inherits from BaseCaching and implements MRU caching
    """

    def __init__(self):

        """
            Initialize the cache
        """

        super().__init__()
        self.usage_order = []

    def put(self, key, item):

        """
            Add an item to the cache using MRU.
            If key or item is None, do nothing.
            If the cache exceeds MAX_ITEMS, discard the MRU
        """

        if key is not None and item is not None:
            if key in self.cache_data:
                self.usage_order.remove(key)

            self.cache_data[key] = item
            self.usage_order.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                mru_key = self.usage_order.pop()
                del self.cache_data[mru_key]
                print(f"DISCARD: {mru_key}")

    def get(self, key):

        """
            Get an item by key.
            If key is None or doesn't exist, return None.
            Update the key as most recently used.
        """

        if key is None or key not in self.cache_data:
            return None

        self.usage_order.remove(key)
        self.usage_order.append(key)
        return self.cache_data[key]
