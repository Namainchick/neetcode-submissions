class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        result = 0
        print(count)
        for i in count:
            if count[i] % 2 == 0:
                result += 1

        return result + 1