#!/usr/bin/env python3
"""
LFU Caching
"""
from collections import defaultdict
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    a class LFUCache that inherits from BaseCaching
    """
    def __init__(self):
        """
        constructor
        """
        super().__init__()
        self.freq_count = defaultdict(int)
        self.frequency = defaultdict(list)
        self.min_freq = 0

    def put(self, key, item):
        """
        a method put that assigns to the dictionary self.cache_data
        """
        if key is None or item is None:
            return

        # Update cache
        if key in self.cache_data:
            self.cache_data[key] = item
            self.freq_count[key] += 1
        else:
            # Evict LFU item if cache is full
            if len(self.cache_data) >= self.MAX_ITEMS:
                while self.frequency[self.min_freq] == []:
                    self.min_freq += 1
                discard = self.frequency[self.min_freq].pop(0)
                del self.cache_data[discard]
                del self.freq_count[discard]
                print("DISCARD: {}".format(discard))

            # Add new item to cache
            self.cache_data[key] = item
            self.freq_count[key] = 1
            self.min_freq = 1

        # Update frequency dictionary
        self.frequency[self.freq_count[key]].append(key)

    def get(self, key):
        """
        a method get that returns the value in self.cache_data linked to key
        """
        if key is None or key not in self.cache_data:
            return None

        # Update frequency
        self.freq_count[key] += 1
        self.frequency[self.freq_count[key]].append(key)

        # Remove key from previous frequency list
        prev_freq = self.freq_count[key] - 1
        self.frequency[prev_freq].remove(key)

        # Update min_freq if necessary
        if not self.frequency[self.min_freq]:
            self.min_freq += 1

        return self.cache_data[key]
