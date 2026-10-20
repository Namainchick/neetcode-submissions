class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        seach all subs and store in cache then check the other one and safe longest. 
        this take 2^n time and space
        we need something better tho.
        maybe we just try the best possible 
        the best would be len of shortest and then search with binary search.
        to check if there are are subsets of length x it takes 2^n - to place n-x in n 
        """
        n = len(text1)
        m = len(text2)
        dp = {}

        def dfs(i,j):
            if i == n or j == m:
                return 0

            if (i,j) in dp:
                return dp[(i,j)]

            res = 0
            if text1[i] == text2[j]:
                res =  1 + dfs(i+1,j+1)
            
            else:
                res = max(dfs(i+1,j),dfs(i,j+1))

            dp[(i,j)] = res
            return res

        return dfs(0,0)