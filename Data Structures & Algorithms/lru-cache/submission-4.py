class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.cache = []
        self.size = 0
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        return self.hashmap.get(key,-1)

    def put(self, key: int, value: int) -> None:
        print(self.cache)
        if self.size == self.capacity:
            last_key = self.cache.pop(0)
            temp = self.hashmap.pop(last_key,None)
        else:
            self.size += 1
        self.hashmap[key] = value
        self.cache.append(key)
        


