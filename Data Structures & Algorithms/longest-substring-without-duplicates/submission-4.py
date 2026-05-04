class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = defaultdict(int)
        best = 0
        l = 0

        for r in range(len(s)):
            seen[s[r]] += 1
            while len(seen) < r-l+1:
                if seen[s[l]] == 1:
                    seen.pop(s[l])
                    l+=1
                else:
                    seen[s[l]] -= 1
                    l += 1
            
            best = max(best,r-l+1)
            print(s[l:r+1],len(seen),r-l+1,best)
        
        return best

        