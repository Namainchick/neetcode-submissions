class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        result = 0
        bucket = set([(x,y) for x,y in points])
        bucket.add((0,0))

        heap = [(0,0,0)]

        while len(bucket) > 0:
            cost,xi,yi = heapq.heappop(heap)
            if (xi,yi) in bucket:
                bucket.remove((xi,yi))
                result += cost
                for xj,yj in bucket:
                    dist = abs(xi-xj) + abs(yi-yj)
                    heapq.heappush(heap,(dist,xj,yj))
                
        return result

