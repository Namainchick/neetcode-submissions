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
                    
"""
ich wäre da niemals selber drauf gekommen mit floyds cycle detection
ich bin nur auf darauf gekommen die indexe des arrays zu nutzen aber dann hätte ich nums makieren müssen 
"""