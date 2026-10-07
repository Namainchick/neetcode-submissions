class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        """
        [[1,3],[2,3],[3,7],[6,6]]

        """
        result = []
        heap = []
        countmap = {}

        intervals.sort(key=lambda x:x[0])
        i = 0
        
        for q in sorted(queries):
            while i < len(intervals)and intervals[i][0] <= q:
                s, e = intervals[i]
                heapq.heappush(heap, (e - s + 1, e))
                i += 1
            while heap and heap[0][1] < q:
                heapq.heappop(heap)
            
            countmap[q] = -1 if not heap else heap[0][0]

        for q in queries:
            result.append(countmap[q])
        
        return result 