class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(nums):
            if target - n in seen:   # erst lookup
                return [seen[target - n], i]
            seen[n] = i