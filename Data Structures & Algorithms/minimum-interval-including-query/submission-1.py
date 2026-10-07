class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        """
        [[1,3],[2,3],[3,7],[6,6]]

        """
        result = []

        shortest_counter = {}

        for start,end in intervals:
            diff = end-start+1
            for i in range(start,end+1):
                if i in shortest_counter:
                    shortest_counter[i] = min(shortest_counter[i],diff)
                else:
                    shortest_counter[i] = diff

        for q in queries:
            result.append(shortest_counter.get(q,-1))

        return result

        