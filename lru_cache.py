from collections import deque
from collections import Counter

class UniqueEltQueue:
    def __init__(self):
        self.counter = Counter()
        self.queue = deque()

    def enq(self, value):
        self.counter.update([value])  # O(1)
        self.queue.appendleft(value)  # O(1)

    def deq(self):
        candidate = self.queue.pop()
        
        # Counter get and queue pop operations are O(1). 
        # While loop eliminates non-unique elements and can be considered as O(1). 
        while self.counter.get(candidate) > 1:    
            candidate = self.queue.pop()  
        return candidate 


class LRU_Cache:
    def __init__(self, capacity):
        # Initialize class variables
        self.cache = {}
        self.capacity = capacity
        self.use_order = UniqueEltQueue()

    def get(self, key):
        # Retrieve item from provided key. Return -1 if nonexistent. 
        value = self.cache.get(key)
        if value is None:
            # Cache miss
            return -1
        # Cache hit
        self.use_order.enq(key) 
        return value

    def set(self, key, value):
        # Set the value if the key is not present in the cache. If the cache is at capacity remove the oldest item. 
        if key in self.cache:
            return
        if len(self.cache) == self.capacity:
            lru_key = self.use_order.deq()
            self.cache.pop(lru_key)

        self.cache[key] = value
        self.use_order.enq(key)


if __name__ == "__main__":
    our_cache = LRU_Cache(5)

    our_cache.set(1, 1)
    our_cache.set(2, 2)
    our_cache.set(3, 3)
    our_cache.set(4, 4)

    print(our_cache.get(1))       # returns 1
    print(our_cache.get(2))       # returns 2
    print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

    our_cache.set(5, 5) 
    our_cache.set(6, 6)

    print(our_cache.get(3))      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
