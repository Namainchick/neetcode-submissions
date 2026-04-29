class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for j,i in enumerate(nums): 
            hash[i] = j
        for i in nums:
            if target - i in hash:
                return [hash[i],hash[target-i]]