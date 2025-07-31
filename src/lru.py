#!/usr/bin/env python3
from typing import Any, Optional
from collections import OrderedDict

class LRUCache:
    """
    A Least Recently Used (LRU) cache keeps items in the cache until it reaches its size
    and/or item limit (only item in our case). In which case, it removes an item that was accessed
    least recently.
    An item is considered accessed whenever `has`, `get`, or `set` is called with its key.

    Implement the LRU cache here and use the unit tests to check your implementation.
    """

    def __init__(self, item_limit: int):
        self.item_limit = item_limit
        self.cache = OrderedDict()

    def has(self, key: str) -> bool:
        if key in self.cache:
            self.cache.move_to_end(key)
            return True
        return False

    def get(self, key: str) -> Optional[Any]:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return None

    def set(self, key: str, value: Any):
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.item_limit:
            self.cache.popitem(last=False)

