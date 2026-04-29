class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash = {}
        for j,i in enumerate(nums): 
            if i in hash:
                hash[i].append[j]
            hash[i] = [j]
        print(hash)
        for i in nums:
            if target - i in hash:
                if i*2 == target:
                    return [hash[i][0],hash[i][1]]
                return [hash[i][0],hash[target-i][0]]