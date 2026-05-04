class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = defaultdict(int)
        best = 0
        l = 0

        for r in range(len(s)):
            if s[r] in seen and l <= seen[s[r]]:
                l = seen[s[r]] + 1
            seen[s[r]] = r
            best = max(best,r-l+1)
        return best        