class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        l,r = 0,0
        res = 0

        while r < n - 1:
            best = 0
            for i in range(l,r+1):
                best = max(best,i+nums[i])

            l,r = r+1,best
            res += 1

        return res

