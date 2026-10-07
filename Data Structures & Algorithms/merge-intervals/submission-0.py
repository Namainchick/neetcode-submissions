class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        result = []

        start,end = 0,0

        for i in range(len(intervals)):
            cur_start,cur_end = intervals[i]
            if end < cur_start:
                result.append([start,end])
                start,end = cur_start,cur_end
            else:
                start = min(cur_start,start)
                end = max(cur_end,end)
        
        result.append([start,end])
        return result[1:]