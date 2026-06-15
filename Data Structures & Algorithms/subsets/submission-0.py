class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        temp = []
        def backtrack(index: int):
            if index >= len(nums):
                result.append(temp.copy())
                return 

            temp.append(nums[index])
            backtrack(index + 1)

            temp.pop()
            backtrack(index + 1)
        backtrack(0)
        return result