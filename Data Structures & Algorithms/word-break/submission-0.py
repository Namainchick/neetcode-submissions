class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [True] + [False] * n

        def checkword(word,index):
            if len(word) + index > n:
                return False
            for c in word:
                if c != s[index]:
                    return False
                index += 1
            return True

        for i in range(n+1):
            if dp[i]:
                for word in wordDict:
                    if checkword(word,i):
                        dp[i+len(word)] = True
        return dp[n]