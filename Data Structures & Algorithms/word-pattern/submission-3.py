class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        hashmap = {}
        if len(words) != len(pattern):
            return False
        for i in range(len(pattern)):
            p = pattern[i]
            w = words[i]
            if w not in hashmap:
                hashmap[w] = p
            else:
                if hashmap[w] != p:
                    return False
        return True
                