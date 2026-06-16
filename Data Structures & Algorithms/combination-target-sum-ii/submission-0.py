class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(index: int, temp: list):
            s = sum(temp)
            if s == target:
                for i in result:
                    if set(i) == set(temp):
                        return 
                result.append(temp.copy())
                return 
            for i in range(index, len(candidates)):
                if s > target:
                    continue
                temp.append(candidates[i])
                backtrack(i+1, temp)
                temp.pop()
        backtrack(0,[])
        return result