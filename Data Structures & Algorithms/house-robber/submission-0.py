class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        def dfs(index):
            if index >= n:
                return 0 

            return max(dfs(index+1),dfs(index+2)+nums[index])

        return dfs(0)