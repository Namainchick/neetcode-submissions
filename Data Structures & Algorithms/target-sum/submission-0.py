from functools import cache
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        @cache
        def dfs(index,cur):
            if index == n:
                return 1 if target == cur else 0
                
            return dfs(index+1,cur-nums[index]) + dfs(index+1,cur+nums[index])
            
        return dfs(0,0)