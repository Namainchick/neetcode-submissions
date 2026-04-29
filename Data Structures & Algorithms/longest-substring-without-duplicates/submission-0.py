class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        result = 0
        best = 0
        start = 0
        sub = ""
        while start + best < len(s):
            if s[start+best] not in sub:
                sub += s[start+best]
                best += 1
                print(sub,best)
            else:
                start += 1
                sub = ""
                result = max(result,best)
                best= 0

        return result
            