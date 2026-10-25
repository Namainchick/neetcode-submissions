from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        borders = [1] + nums + [1]
        
        dp = [[-1] * (n+2) for _ in range(n+2)]
        def dfs(l,r):
            best = 0
            if dp[l][r] != -1:
                return dp[l][r]

            for i in range(l,r+1):
                cur = borders[l-1] * borders[i] * borders[r+1] + dfs(l,i-1) + dfs(i+1,r)
                best = max(best,cur)
            
            dp[l][r] = best
            return best

        return dfs(1,n)