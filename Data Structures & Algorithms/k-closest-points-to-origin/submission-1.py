class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def calc(x,y):
            return math.sqrt(x**2 + y**2)

        heap = []
        for point in points:
            x = point[0]
            y = point[1]
            heapq.heappush(heap,(calc(x,y),point))

        return [foo for _,foo in heapq.nsmallest(k,heap)]

"""
bruh i dont like heaps 
"""