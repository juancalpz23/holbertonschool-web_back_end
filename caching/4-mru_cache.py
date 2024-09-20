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
        self.most_recent = None

    def put(self, key, item):

        """
            Add an item to the cache using MRU.
            If key or item is None, do nothing.
            If the cache exceeds MAX_ITEMS, discard the (MRU).
        """
    
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data[key] = item
            else:
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    print(f"DISCARD: {self.most_recent}")
                    del self.cache_data[self.most_recent]

                self.cache_data[key] = item

            self.most_recent = key

    def get(self, key):

        """
            Get an item by key.
            If key is None or doesn't exist, return None.
            Update the key as most recently used.
        """

        if key is None or key not in self.cache_data:
            return None

        self.most_recent = key
        return self.cache_data[key]
