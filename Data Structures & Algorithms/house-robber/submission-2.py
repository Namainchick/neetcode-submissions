class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        """cache = {}

        def dfs(index):
            if index >= n:
                return 0

            if index in cache:
                return cache[index] 

            cache[index] = max(dfs(index+1),dfs(index+2)+nums[index])
            return cache[index] 

        return dfs(0)"""

        nxt1,nxt2 = 0,0
        for x in reversed(nums):
            nxt1,nxt2 = max(x+nxt2,nxt1),nxt1

        return nxt1