class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        result = -float('inf')
        if n == 0:
            return 0

        index = 0
        cur = 1
        while index < n:
            if nums[index] == 0:
                cur = 0
            else:
                cur *= nums[index]
            result = max(result,cur)
            index += 1

        index = n-1
        cur = 1
        while index >= 0:      
            if nums[index] == 0:
                cur = 0
            else:
                cur *= nums[index]
            result = max(result,cur)
            index -= 1

        return result 

        

