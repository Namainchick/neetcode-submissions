class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        mid = len(nums) // 2
        l,r = 0,len(nums)

        while l < r:
            mid = (l + r) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l  = mid + 1
            else:
                r = mid - 1


        if nums[mid] > target:
            return mid-1
        else:
            return mid+1
