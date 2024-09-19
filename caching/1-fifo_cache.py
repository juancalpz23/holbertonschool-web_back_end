#!/usr/bin/python3


"""
    FIFOCache module
"""


from base_caching import BaseCaching


class FIFOCache(BaseCaching):

    """
        FIFOCache inherits from BaseCaching and implements a FIFO caching system.
    """

    def __init__(self):
    
        """
            Initialize the cache
        """

        super().__init__()
        self.keys_order = []

    def put(self, key, item):

        """
            Add an item to the cache using FIFO.
            If key or item is None, do nothing.
            If the cache exceeds MAX_ITEMS, discard the first item added (FIFO).
        """

        if key is not None and item is not None:
            if key not in self.cache_data:
                self.keys_order.append(key)

            self.cache_data[key] = item

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = self.keys_order.pop(0)  # Remove the first added key
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")

    def get(self, key):

        """
            Get an item by key.
            If key is None or doesn't exist, return None.
        """

        return self.cache_data.get(key, None)
