class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:  
        best = 0
        l,r = 0,0
        current = {}
        while l <= r and r < len(s):
            if s[r] not in current:
                current[s[r]] = r
                r += 1
            else:
                temp = current.pop(s[r])
                l = temp
            best = max(best,r-l)

        return best - 1 