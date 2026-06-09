class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        for stone in stones:
            heapq.heappush(heap, -stone)
        while len(heap) > 1:  
            foo = -heapq.heappop(heap)
            bar = -heapq.heappop(heap)

            if foo > bar:
                heapq.heappush(heap,foo-bar)
            if bar > foo:
                heapq.heappush(heap,bar-foo)
        if heap:
            return heap[0]
        else:
            return 0
            