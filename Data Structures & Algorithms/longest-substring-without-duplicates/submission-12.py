class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:  
        if len(s) <= 1:
            return len(s)
        best = 0
        l,r = 0,0
        current = {}
        while l <= r and r < len(s):
            

            if s[r] not in current:
                best = max(best,r-l)
                current[s[r]] = r
                r += 1
            else:
                temp = current.pop(s[r])
                l = temp
            

        return best 