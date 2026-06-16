class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(index, temp):
            s = sum(temp)
            if s == target:
                result.append(temp.copy())
            for i in range(index, len(nums)):
                if s <= target:
                    temp.append(nums[i])
                    backtrack(i, temp)
                    temp.pop()
        backtrack(0,[])
        return result