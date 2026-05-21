class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.cache = []
        self.size = 0
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        return self.hashmap.get(key,-1)

    def put(self, key: int, value: int) -> None:
        if self.size == self.capacity:
            last_key = self.cache.pop(0)
            del self.hashmap[last_key]
        else:
            self.size += 1
        self.hashmap[key] = value
        self.cache.append(key)
        


