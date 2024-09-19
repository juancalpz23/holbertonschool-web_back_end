#!/usr/bin/python3


"""
    LIFOCache module
"""


from base_caching import BaseCaching


class LIFOCache(BaseCaching):

    """
        LIFOCache inherits from BaseCaching and implements LIFO caching
    """

    def __init__(self):

        """
            Initialize the cache
        """

        super().__init__()
        self.last_key = None  # Track the last inserted key

    def put(self, key, item):

        """
            Add an item to the cache using LIFO.
            If key or item is None, do nothing.
            If the cache exceeds MAX_ITEMS, discard the last item added LIFO
        """

        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                if self.last_key is not None:
                    del self.cache_data[self.last_key]
                    print(f"DISCARD: {self.last_key}")

            self.last_key = key  # Update the last inserted key

    def get(self, key):

        """
            Get an item by key.
            If key is None or doesn't exist, return None.
        """

        return self.cache_data.get(key, None)
