class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash1 = self.counter(s)
        hash2 = self.counter(t)
        return hash1 == hash2
    
    def counter(self,string: str):
        hash = {}
        for c in string:
            if c in hash:
                hash[c] = hash[c] + 1
            else:
                hash[c] = 1
        return hash