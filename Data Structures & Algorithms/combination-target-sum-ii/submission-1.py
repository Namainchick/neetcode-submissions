class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()

        def backtrack(index: int, temp: list):
            s = sum(temp)
            if s == target:
                result.append(temp.copy())
                return 

            for i in range(index, len(candidates)):
                if s > target:
                    break
                if i > index and candidates[i] == candidates[i-1]:
                    continue
                temp.append(candidates[i])
                backtrack(i+1, temp)
                temp.pop()

        backtrack(0,[])
        return result