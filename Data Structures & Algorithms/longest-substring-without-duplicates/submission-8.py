class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        best = 0
        l,r = 0,0
        current = {}
        while l <= r and r < len(s):
            best = max(best,r-l)
            if s[r] not in current:
                current[s[r]] = r
                r += 1
            else:
                temp = current.pop(s[r])
                l = temp
            

        return best - 1