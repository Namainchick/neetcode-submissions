class Solution:
    def canJump(self, nums: List[int]) -> bool:
        index = 0
        jumps = 0
        l = len(nums)
        while jumps >= 0:
            if index == l-1:
                return True
            jumps = max(jumps,nums[index])
            index += 1
            jumps -= 1

        return False


            
        