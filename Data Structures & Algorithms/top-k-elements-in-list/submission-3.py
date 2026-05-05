class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [0] * (len(nums) + 1)
        sol = []
        counter = defaultdict(int)
        for i in nums:
            counter[i] += 1 
        for i in counter:
            bucket[counter[i]] = i
        counter = 0
        for i in range(len(nums),-1,-1):
            if counter == k:
                break
            if bucket[i] > 0:
                sol.append(bucket[i])
                counter += 1


        return sol