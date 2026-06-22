class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:  
        best = 0
        l,r = 0,0
        current = {}
        while r < len(s):
            
            if s[r] in current and current[s[r]] >= l:
                l = current[s[r]] + 1
            current[s[r]] = r
            best = max(best, r - l + 1)
            r += 1

        return best 