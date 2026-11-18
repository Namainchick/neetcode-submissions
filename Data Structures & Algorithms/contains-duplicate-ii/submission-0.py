class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(n):
            for l in range(1,k+1):
                j = i + l
                if j < n and nums[j] == nums[i]:
                    return True
        return False 