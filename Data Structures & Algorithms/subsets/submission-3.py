class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.result = []

        def backtrack(index,temp):
            self.result.append(temp.copy())

            for i in range(index,len(nums)):
                temp.append(nums[i])
                backtrack(i+1,temp)
                temp.pop()

        backtrack(0,[])
        return self.result