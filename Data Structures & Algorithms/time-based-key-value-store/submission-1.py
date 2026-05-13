class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key].append((value,timestamp))
        else:
            for i in range(len(self.hashmap[key])):
                _,time = self.hashmap[key][i]
                if timestamp <= time:
                    self.hashmap[key].insert(i,(value,timestamp))
                    return 
        self.hashmap[key].append((value,timestamp))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        else:
            for i in range(len(self.hashmap[key])-1,-1,-1):
                val,time = self.hashmap[key][i]
                if timestamp >= time:
                    return val
        return ""
