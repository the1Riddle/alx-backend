#!/urs/bin/env python3
"""
FIFO caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO cache class
    """
    def __init__(self):
        """
        FIFO cache class constructor
        """
        super().__init__()
        self.cache_list = []

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = self.cache_list.pop(0)
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))

            self.cache_data[key] = item
            self.cache_list.append(key)

    def get(self, key):
        """
        Get an item by key
        """
        return self.cache_data.get(key, None)
