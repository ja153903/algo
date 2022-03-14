"""
We can keep the items we set in a map
So that we have O(1) lookup

If the value doesn't exist within the map, then
we should just return -1

Whenever we access an existing key, we should update
its position in our LRU. One way we can do this in Python,
is to remove the key-value pair from the dictionary and reinsert.
This is because insertion into a dictionary in python is deterministic.
"""


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.cache = {}
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        value = self.cache[key]

        self._update_lru(key)

        return value

    def _update_lru(self, key: int) -> None:
        if key in self.cache:
            value = self.cache[key]

            del self.cache[key]

            self.cache[key] = value

    def get_lru(self) -> int:
        for key in self.cache.keys():
            yield key

    def _evict_lru(self) -> None:
        lru = next(self.get_lru())

        if lru in self.cache:
            del self.cache[lru]

    def put(self, key: int, value: int) -> None:
        size = len(self.cache)

        if size == self.capacity and key not in self.cache:
            self._evict_lru()

        self.cache[key] = value

        self._update_lru(key)
