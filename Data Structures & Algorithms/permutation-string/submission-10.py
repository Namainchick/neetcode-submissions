class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        foo = Counter(s1)
        bar = Counter(s2[:len(s1)])

        for i in range(len(s2)-len(s1)):
            if i > 0:
                bar[s2[i-1]] -= 1
                bar[s2[i+len(s1)-1]] += 1
                
            print(bar,foo)
            if bar == foo:
                return True
        return False