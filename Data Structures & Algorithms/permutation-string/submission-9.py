class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        foo = Counter(s1)
        for i in range(len(s2)-len(s1)+1):
            print(Counter(s2[i:i+len(s1)]),foo)
            if foo == Counter(s2[i:i+len(s1)]):
                return True
        return False