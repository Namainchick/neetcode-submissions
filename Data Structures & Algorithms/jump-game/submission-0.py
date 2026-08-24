class Solution:
    def canJump(self, nums: List[int]) -> bool:
        index = 0
        jumps = 0
        l = len(nums)
        while jumps >= 0:
            jumps = max(jumps,nums[index])
            index += 1
            jumps -= 1

        return index > l-1
            
        