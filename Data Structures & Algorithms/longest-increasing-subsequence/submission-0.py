class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        for i in range(n):
            best = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    best = max(nums[j],best)
            dp[i] = best + 1

        return max(dp)