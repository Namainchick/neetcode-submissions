class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash = {}
        for i in nums:
            if i in hash:
                hash[i] = hash[i] + 1
            else: hash[i] = 1
        
        buckets = [[] for _ in range(0,len(nums)+1)]
        for i,j in hash.items():
            buckets[j].append(i)
        result = []
        for i in range(len(buckets) - 1, -1, -1):
            if buckets[i] != []:
                result.append(buckets[i][0])
                if len(result) == k:
                    return result
