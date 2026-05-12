class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            num = nums[mid]
            if num == target:
                return mid
            
            if num >= nums[l]:                   # linke Hälfte sortiert
                if nums[l] <= target < num:
                    r = mid - 1
                else:
                    l = mid + 1
            else:                                # rechte Hälfte sortiert
                if num < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        
        return -1

# pls do again cant understand hwo this shit is implemented i understand the trick but not how it can be inplemented