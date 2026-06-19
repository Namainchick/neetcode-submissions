class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        hashmap = {}
        for i in range(len(pattern)):
            p = pattern[i]
            w = words[i]
            if p not in hashmap:
                hashmap[p] = w
            else:
                if hashmap[p] != w:
                    return False
        return True
                