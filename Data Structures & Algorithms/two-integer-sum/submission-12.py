class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for j,i in enumerate(nums): 
            if i in hash:
                pass
            else: hash[i] = j
        print(hash)
        for j,i in enumerate(nums):
            if target - i in hash :
                return [hash[target-i],j]