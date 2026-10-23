class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """

        "caaat", t = "cat"

        """

        def dfs(i,j):
            if s[i] == s[j]:
                return 