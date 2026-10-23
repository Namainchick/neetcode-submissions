from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        if n1+n2 == len(s3):
            return False

        @cache
        def dfs(i,j):
            if i == n1 and j == n2:
                return True
            k = i + j

            if i < n1 and s1[i] == s3[k] and dfs(i+1,j):
                return True
            if j < n2 and s2[j] == s3[k] and dfs(i,j+1):
                return True

            return False

        return dfs(0,0)
            
