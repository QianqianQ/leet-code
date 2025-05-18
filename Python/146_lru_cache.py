class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.prev = self.next = self

    def get(self, key: int) -> int:
        if key in self.cache:
            res_node = self.cache[key]
            self._remove(res_node)
            self._add(res_node)
            return res_node.val

        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        n = Node(key, value)
        self._add(n)
        self.cache[key] = n
        if len(self.cache) > self.capacity:
            n = self.next
            self._remove(n)
            del self.cache[n.key]

    def _remove(self, node):
        p = node.prev
        n = node.next
        p.next = n
        n.prev = p

    def _add(self, node):
        p = self.prev
        p.next = node
        self.prev = node
        node.prev = p
        node.next = self


if __name__ == '__main__':
    # Example usage
    lru_cache = LRUCache(2)
    lru_cache.put(1, 1)  # cache is {1=1}
    lru_cache.put(2, 2)  # cache is {1=1, 2=2}
    print(lru_cache.get(1))  # return 1
    lru_cache.put(3, 3)  # evicts key 2, cache is {1=1, 3=3}
    print(lru_cache.get(2))  # return -1 (not found)
    lru_cache.put(4, 4)  # evicts key 1, cache is {4=4, 3=3}
    print(lru_cache.get(1))  # return -1 (not found)
    print(lru_cache.get(3))  # return 3
    print(lru_cache.get(4))  # return 4
