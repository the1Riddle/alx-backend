#!/usr/bin/env python3
"""
LRU caching
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    class LRUCache that inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """
        constructor
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data the item value for the key
        """
        if key and item:
            if key in self.cache_data:
                self.order.remove(key)
            self.cache_data[key] = item
            self.order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                del_key = self.order.pop(0)
                del self.cache_data[del_key]
                print("DISCARD: {}".format(del_key))

    def get(self, key):
        """
        return the value in self.cache_data linked to key
        """
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
