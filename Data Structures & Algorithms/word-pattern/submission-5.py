class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        hashmap = {}
        if len(words) != len(pattern):
            return False
        for i in range(len(pattern)):
            p = pattern[i]
            w = words[i]
            if p not in hashmap and w not in hashmap.values():
                hashmap[p] = w
            else:
                if not hashmap[p] or hashmap[p] != w:
                    return False
        return True
                