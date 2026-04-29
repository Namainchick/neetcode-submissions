class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0*n]
        for i,n in enumerate(nums):
            ans[i] = nums[i%n]
            return ans