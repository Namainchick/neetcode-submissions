"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        """
        - sort the intervals by start time. (sort array)
        - whoever is first gets a room. 
        - if the next clashes with the one after add a room. there is now way around it. 
        - we need keep track of the earliest finishing room so we know if we can use a room or if we 
        - we need another one. (heap)

        example.
        [(0,40),(5,10),(15,20)]

        heap: (15,20),(0,40)

        """

        intervals.sort(key=lambda x:x.start)
        heap = []

        for i in intervals:

            if heap and i.start >= heap[0]:
                heapq.heappop(heap)

            heapq.heappush(heap,i.end)
        
        return len(heap)
