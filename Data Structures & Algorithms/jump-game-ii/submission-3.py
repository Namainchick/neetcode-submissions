from functools import cache
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        wave = 0 
        r = 0
        i = 0

        while i < n:
            best = 0
            while i <= r and i < n:
                best = max(best,i+nums[i])
                i += 1
            r = best
            wave += 1

        return wave - 1

