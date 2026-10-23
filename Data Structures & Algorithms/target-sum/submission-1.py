class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)

        dp = {}
        def dfs(index,cur):
            if (index,cur) in dp:
                return dp[(index,cur)]
            if index == n:
                return 1 if target == cur else 0
                
            sol = dfs(index+1,cur-nums[index]) + dfs(index+1,cur+nums[index])
            dp[(index,cur)] = sol 

            return sol
            
        return dfs(0,0)