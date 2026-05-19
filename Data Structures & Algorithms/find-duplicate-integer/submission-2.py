class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        fast,slow = 0,0

        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]

            if fast == slow:
                fast = 0
                while True:
                    if slow == fast:
                        return fast
                    fast = nums[fast]
                    slow = nums[slow]
                    
                    