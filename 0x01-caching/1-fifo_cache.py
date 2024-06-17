#!/usr/bin/env python3
"""Create a class FIFOCache that inherits
from BaseCaching and is a caching system:"""
from base_caching import BaseCaching
from collections import OrderedDict


class FIFOCache(BaseCaching):
    """ a caching system
    """
    def __init__(self):
        """overload previous intialization"""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """this assigns a pair and discards
        if the max is reached"""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            fk, first_item = self.cache_data.popitem(False)
            print("DISCARD: {}".format(fk))

    def get(self, key):
        """retrives value """

        return self.cache_data.get(key, None)
