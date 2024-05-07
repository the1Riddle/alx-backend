#!/usr/bin/env python3
"""
LIFO Caching
"""
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    def __init__(self):
        """
        Constructor
        """
        super().__init__()
        self.cache_stack = []

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key and item:
            if key in self.cache_data: 
                self.cache_stack.remove(key)
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                # Evict the least recently used item
                discard = self.cache_stack.pop()
                del self.cache_data[discard]
                print("DISCARD: {}".format(discard))

            self.cache_data[key] = item
            self.cache_stack.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache
        """
        if key in self.cache_data:
            # Move the accessed item to the top of the stack
            self.cache_stack.remove(key)
            self.cache_stack.append(key)
            return self.cache_data[key]
        return None
