class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.cache = []
        self.size = 0
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        return self.hashmap.get(key,-1)

    def put(self, key: int, value: int) -> None:
        if self.size < self.capacity:
            self.hashmap[key] = value
            self.cache.append(key)
            self.size += 1
        else:
            last_key = self.cache.pop(0)
            last_val = self.hashmap[last_key]
            del self.hashmap[last_key]
        


