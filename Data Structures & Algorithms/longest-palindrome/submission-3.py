class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        result = 0
        temp = 0
        print(count)
        for i in count:
            result +=  count[i] - count[i] % 2
            if count[i] % 2 == 1:
                temp += 1
        return result if temp == 0 else result + 1


