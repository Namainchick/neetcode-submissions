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

"""
I kinda understand but also not really
def backtrack(zustand):
    # STELLE 1: Wann speichern?
    if ...:
        result.append(zustand.copy())
        return
    
    for wahl in mögliche_wahlen:
        # STELLE 2: Ist die Wahl gültig?
        if ungültig: continue
            
        zustand.append(wahl)
        backtrack(...)
        zustand.pop()
"""