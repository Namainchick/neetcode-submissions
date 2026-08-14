class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        l,r = 0,n-1
        result = list()

        while l <= r:
            if abs(nums[l]) > abs(nums[r]):
                result.insert(0,nums[l]*nums[l])
                l += 1
            else:
                result.insert(0,nums[r]*nums[r])
                r -= 1

        return result