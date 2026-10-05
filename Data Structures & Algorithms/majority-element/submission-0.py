class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        current = None
        count = 0 

        for num in nums:
            if current == num:
                count += 1
            elif count == 0:
                current = num
                count = 1
            else:
                count -= 1

        return current