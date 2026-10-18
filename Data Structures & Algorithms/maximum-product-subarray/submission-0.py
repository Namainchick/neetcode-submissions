class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        there are n^2 substrings
        brute force is then n^3 because checking for each is n
        what if can directly calc with prefix then still n^2
        """
        n = len(nums)
        dp = [1] * (n+1)
        result = 0

        for i in range(n):
            dp[i+1] = dp[i] * nums[i]

        for i in range(1,n+1):
            for j in range(1,n+1):
                if dp[i] == 0 or 0 == dp[j]:
                    continue
                sol = dp[j]/dp[i-1]
                result = max(result,sol)

        return int(result)