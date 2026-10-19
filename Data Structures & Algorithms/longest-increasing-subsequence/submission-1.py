class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [1] * n

        for i in range(n):
            best = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    best = max(dp[j],best)
            dp[i] = best + 1

        return max(dp)

"""
[9,1,4,2,3,3,7]
[1,1,2,2,3,3,1]
           i
         j

"""