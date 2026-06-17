class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrack(temp, remain):
            if not remain:
                result.append(temp.copy())
            for i in range(len(remain)):
                temp.append(remain[i])
                backtrack(temp, remain[:i] + remain[i+1:])
                temp.pop()
        backtrack([], nums.copy())
        return result