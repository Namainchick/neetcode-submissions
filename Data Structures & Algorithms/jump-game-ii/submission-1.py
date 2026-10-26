from functools import cache
class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        this could be done by recursion. with a cashe i would be O(n) time 
        """
        n = len(nums)

        @cache
        def dfs(i):
            if i == n-1:
                return 1 
            
            jump = nums[i]

            best = float('inf')
            for j in range(i+1,i+jump+1):
                if j < n:
                    best = min(best,dfs(j))

            return best + 1

        return dfs(0) - 1
    