class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums)-1

        while left < right:
            mid  = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid


        return nums[right]

#very hard to understand how the strucure can help find the min. also indexes where hard to wrap head around
