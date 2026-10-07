class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        [[1,2],[2,4],[1,4]]
        """

        intervals.sort(key=lambda x:x[1])
        result = 0
        _,prev_end = intervals[0]

        for i in range(1,len(intervals)):
            start,end = intervals[i]
            if start >= prev_end:
                prev_end = end
            else:
                result += 1

        return result

