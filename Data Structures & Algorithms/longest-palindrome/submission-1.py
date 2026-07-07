class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        result = 0
        print(count)
        for i in count:
            if count[i] % 2 == 0:
                result += count[i]

        return result + 1