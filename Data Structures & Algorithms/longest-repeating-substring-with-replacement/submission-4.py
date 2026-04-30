class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #sliding window
        l = 0 
        r = 0
        best = 0
        out = 0
        while l<=r and l+r <= len(s):
            if s[r] == s[l]:
                r += 1
            elif out < k:
                out += 1
                r += 1
                
            elif s[l+1] != s[l]:
                l += 1
                out = 0

            else:
                l += 1
            best = max(best,r-l)
            print(l,r,best)
        return best
                
