class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket = [0] * 1000
        sol = []
        for i in nums:
            bucket[i] += 1
        counter = 0
        for i in range(999,-1,-1):
            if counter == k:
                break
            if bucket[i] > 0:
                sol.append(i)
                counter += 1


        return sol