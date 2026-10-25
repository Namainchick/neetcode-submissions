from functools import cache
class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        borders = [1] + nums + [1]
        
        def dfs(l,r):
            best = 0

            for i in range(l,r+1):
                cur = borders[l-1] * borders[i] * borders[r+1] + dfs(l,i-1) + dfs(i+1,r)
                best = max(best,cur)
            
            return best

        return dfs(1,n)