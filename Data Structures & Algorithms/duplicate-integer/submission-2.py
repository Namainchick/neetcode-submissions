class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            if i >= 1 and nums[i] == nums[i-1]:
                return False

        return True
                