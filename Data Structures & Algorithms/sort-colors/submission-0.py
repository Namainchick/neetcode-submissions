class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            color = nums[i]
            if color != 0:
                j = i
                while j < len(nums) - 1 and nums[j] != 0:
                    j += 1
                nums[i],nums[j] = nums[j],nums[i]

        for i in range(len(nums)-1,-1,-1):
            color = nums[i]
            if color != 2:
                j = i
                while j > 0 and nums[j] != 2:
                    j -= 1
                nums[i],nums[j] = nums[j],nums[i]

