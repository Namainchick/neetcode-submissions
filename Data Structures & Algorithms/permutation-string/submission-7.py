class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        foo = set(s1)
        for i in range(len(s2)-len(s1)+1):
            print(set(s2[i:i+len(s1)]),foo)
            if foo == set(s2[i:i+len(foo)]):
                return True
        return False