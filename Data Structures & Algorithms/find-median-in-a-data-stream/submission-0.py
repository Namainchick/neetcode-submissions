class MedianFinder:

    def __init__(self):
        self.big = []
        self.small = []

    def addNum(self, num: int) -> None: 
        heapq.heappush(self.small, -num)
        heapq.heappush(self.big, -heapq.heappop(self.small))
        if len(self.big) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.big))

    def findMedian(self) -> float:
        if len(self.small) > len(self.big):
            return -self.small[0]
        return (-self.small[0] + self.big[0])/2



"""
i am aware of keeping track of bigger and smaller queue but how
""" 