from functools import cache
class Solution:
    @cache
    def maxCoins(self, nums: List[int]) -> int:
        def dfs(cur):
            best = 0
            for i in range(len(cur)):
                left = cur[i-1] if i-1 >= 0 else 1
                right = cur[i+1] if i+1 < len(cur) else 1
                best = max(best,dfs(cur[:i]+ cur[i+1:]) + left * right * cur[i])

            return best
        return dfs(tuple(nums))

