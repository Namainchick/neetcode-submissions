from functools import cache
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)

        @cache
        def dfs(i,j):
            if i == n1 and j == n2:
                return True

            k = i + j + 2

            if i < n1 and s1[i] == s3[k]:
                return True
            if j < n2 and s2[j] == s3[3]:
                return True

            return False

        return dfs(0,0)
            
