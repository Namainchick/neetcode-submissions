class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #sliding window
        l = 0 
        result = 0
        count = defaultdict(int)

        for r in range(len(s)):
            count[s[r]] += 1

            while r-l-max(count.values()) >= k:
                count[s[l]] -= 1
                l += 1
                
            result = max(result,r-l+1)
        return result
