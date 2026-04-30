class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        foo = tuple(s1)
        for i in range(len(s2)-3):
            print(tuple(s2[i:i+len(foo)]),foo)
            if foo == tuple(s2[i:i+len(foo)]):
                return True
        return False