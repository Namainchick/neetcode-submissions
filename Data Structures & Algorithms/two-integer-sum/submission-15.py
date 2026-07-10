class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,num in enumerate(nums):
            counter = target - num
            if counter in hashmap:
                return [hashmap[counter],i]
            hashmap[num] = i