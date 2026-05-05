class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        sol = []
        buckets = [[] for i in range(len(nums)+1)]
        for num,freq in counts.items():
            buckets[freq].append(num)
        print(buckets)
        for i in range(len(nums),-1,-1):
            for j in buckets[i]:
                sol.append(j)
                if len(sol) == k:
                    return sol
        return sol