"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        sort = sorted(intervals, key=lambda x: x.start)
        interval = 0
        for i in sort:
            if i.start >= interval:
                interval = i.end
            else:
                return False
        return True 
