class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        if r == 0:
            return r if nums[r] == target else -1
        while l < r:
            mid = (l+r) // 2
            num = nums[mid]
            if num == target:
                return mid
            if num > nums[l]:
                if nums[l] <= target < num:
                    r = mid
                else:
                    l = mid + 1
            else:
                if num < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid
        return -1