class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(index: int, temp: list):
            result.append(temp.copy())

            for i in range(index,len(nums)):
                temp.append(nums[i])
                backtrack(i+1, temp)
                temp.pop()

        backtrack(0,[])
        return result

"""
how the fuck I cant think anymore its way too late
"""