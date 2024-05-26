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
        """..."""
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            fk, first_item = self.cache_data.popitem
            print("DISCARD:{}".format(fk))

    def get(self, key):
        if key is None:
            return
        return self.cache_data.get(key)