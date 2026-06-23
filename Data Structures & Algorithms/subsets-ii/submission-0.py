class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.result = []
        nums.sort()
        def backtrack(index, current):
            self.result.append(current.copy())
                
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:  # ← duplikat skip
                    continue
                current.append(nums[i])
                backtrack(i+1,current)
                current.pop()
        backtrack(0,[])

        return self.result