class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((value,timestamp))


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        else:
            l = 0
            r = len(self.hashmap[key]) - 1
            res = ""
            while l <= r:
                mid = (l+r) // 2
                val,time = self.hashmap[key][mid]
                if timestamp >= time:
                    res = val
                    l = mid + 1
                else:
                    r = mid - 1
            return res

# this is pretty brute force lets see if theres a better way

